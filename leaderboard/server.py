"""HTTP-server van de leaderboard (Python stdlib, geen externe pakketten).

Start:  py server.py                (poort 8321, adres 0.0.0.0)
Opties: py server.py --port 9000 --wachtwoord "..."

Pagina's:
  /            → weergave voor het groot scherm (ververst zichzelf)
  /registreer  → spelers kiezen hier zelf hun pseudoniem
  /crew        → crew-ingang (wachtwoord), score- en spelerbeheer

Alles draait lokaal op de campusnetwerk (VLAN 20); zie README.md.
"""

import argparse
import http.cookies
import json
import os
import secrets
import threading
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import opslag

_BASIS = os.path.dirname(os.path.abspath(__file__))
_STATISCHE = os.path.join(_BASIS, "static")
_CONFIG = os.path.join(_BASIS, "config.json")

# Eén gedeeld crew-wachtwoord; slaan in config.json (niet in de git-repo).
_lek = threading.Lock()
_sesjes = {}  # token → vervaldatum


def _config_lezen() -> dict:
    if os.path.exists(_CONFIG):
        with open(_CONFIG, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _config_schrijven(cfg: dict) -> None:
    with open(_CONFIG, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def wachtwoord_inrichten(default: str | None = None) -> str:
    """Zorg dat er een crew-wachtwoord is; geeft het terug (voor de console)."""
    cfg = _config_lezen()
    if "wachtwoord" not in cfg or not cfg["wachtwoord"]:
        cfg["wachtwoord"] = default or secrets.token_urlsafe(9)
        _config_schrijven(cfg)
    return cfg["wachtwoord"]


def sessie_nieuw(token: str, duur_minuten: int = 24 * 60) -> None:
    _sesjes[token] = datetime.now() + timedelta(minutes=duur_minuten)


def sessie_geldig(token: str | None) -> bool:
    if not token:
        return False
    met = _sesjes.get(token)
    if met is None:
        return False
    if met < datetime.now():
        del _sesjes[token]  # verlopen: opruimen
        return False
    return True


def sessie_verwijder(token: str) -> None:
    _sesjes.pop(token, None)


class Handler(BaseHTTPRequestHandler):
    server_version = "Leaderboard/1.0"

    # ------------------------------------------------------------ helpers

    def _stuur(self, code: int, lichaam: bytes, inhoud_type: str, extra_koppen: dict | None = None):
        self.send_response(code)
        self.send_header("Content-Type", inhoud_type)
        self.send_header("Content-Length", str(len(lichaam)))
        self.send_header("Cache-Control", "no-store")
        if extra_koppen:
            for k, v in extra_koppen.items():
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(lichaam)

    def _json(self, code: int, data: dict, extra_koppen: dict | None = None):
        self._stuur(code, json.dumps(data, ensure_ascii=False).encode("utf-8"),
                    "application/json; charset=utf-8", extra_koppen)

    def _html(self, pad: str):
        weg = os.path.join(_STATISCHE, pad)
        try:
            with open(weg, "rb") as f:
                data = f.read()
        except OSError:
            self._json(404, {"fout": "Page not found."})
            return
        self._stuur(200, data, "text/html; charset=utf-8")

    def _lichaam_lezen(self) -> dict:
        try:
            lengte = int(self.headers.get("Content-Length", 0))
            ruw = self.rfile.read(lengte).decode("utf-8")
            return json.loads(ruw or "{}")
        except (ValueError, UnicodeDecodeError):
            return {}

    def _crew_cookie(self) -> str | None:
        cookie = http.cookies.SimpleCookie(self.headers.get("Cookie", ""))
        return cookie["crew"].value if "crew" in cookie else None

    # -------------------------------------------------------------- routes

    def do_GET(self):
        pad = self.path.split("?", 1)[0].rstrip("/") or "/"
        if pad == "/":
            self._html("scherm.html")
        elif pad == "/registreer":
            self._html("registreer.html")
        elif pad == "/api/data":
            self._json(200, {
                "games": opslag.top_per_game(),
                "totaal": opslag.totaalstand(),
            })
        elif pad == "/crew":
            if sessie_geldig(self._crew_cookie()):
                self._html("crew.html")
            else:
                self._html("crew-login.html")
        elif pad == "/crew/spelers":
            if sessie_geldig(self._crew_cookie()):
                self._json(200, {"spelers": opslag.spelers()})
            else:
                self._json(401, {"fout": "Crew login required."})
        elif pad == "/crew/recent":
            if sessie_geldig(self._crew_cookie()):
                self._json(200, {"recent": opslag.recent_scores(20)})
            else:
                self._json(401, {"fout": "Crew login required."})
        elif pad.endswith(".js") or pad.endswith(".css"):
            self._statisch(pad.lstrip("/"))
        else:
            self._json(404, {"fout": "Unknown route."})

    def _statisch(self, naam: str):
        """Serveer een statisch bestand (alleen .js/.css) uit static/,
        beschermd tegen pad-traversal."""
        pad = os.path.abspath(os.path.join(_STATISCHE, naam))
        if not pad.startswith(os.path.abspath(_STATISCHE) + os.sep) or not os.path.isfile(pad):
            self._json(404, {"fout": "Not found."})
            return
        data = open(pad, "rb").read()
        type_ = "text/javascript" if pad.endswith(".js") else "text/css"
        self.send_response(200)
        self.send_header("Content-Type", type_ + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        pad = self.path.split("?", 1)[0]
        data = self._lichaam_lezen()
        try:
            if pad == "/crew/aanmelden":
                zelf = wachtwoord_inrichten()
                if secrets.compare_digest(str(data.get("wachtwoord", "")), zelf):
                    token = secrets.token_urlsafe(16)
                    sessie_nieuw(token)
                    self._json(200, {"ok": True},
                               {"Set-Cookie": f"crew={token}; Path=/; HttpOnly; SameSite=Strict; Max-Age=86400"})
                else:
                    self._json(403, {"fout": "Incorrect password."})
            elif not sessie_geldig(self._crew_cookie()):
                self._json(401, {"fout": "Crew login required."})
            elif pad == "/crew/afmelden":
                sessie_verwijder(self._crew_cookie())
                self._json(200, {"ok": True}, {"Set-Cookie": "crew=; Path=/; Max-Age=0"})
            elif pad == "/crew/game":
                gid = opslag.nieuwe_game(str(data.get("naam", "")))
                self._json(200, {"ok": True, "id": gid})
            elif pad == "/crew/game/verwijder":
                ok = opslag.verwijder_game(str(data.get("id", "")))
                self._json(200 if ok else 404, {"ok": ok})
            elif pad == "/crew/speler":
                sid = opslag.voeg_speler_toen(str(data.get("naam", "")))
                self._json(200, {"ok": True, "id": sid})
            elif pad == "/crew/score":
                meting = opslag.bewaar_score(
                    str(data.get("game_id", "")),
                    str(data.get("naam", "")),
                    data.get("waarde"),
                )
                self._json(200, {"ok": True, "id": meting["id"]})
            elif pad == "/crew/score/verwijder":
                ok = opslag.verwijder_score(str(data.get("id", "")))
                self._json(200 if ok else 404, {"ok": ok})
            elif pad == "/crew/speler/verwijder":
                aantal = opslag.verwijder_speler(str(data.get("id", "")))
                self._json(200, {"ok": True, "verwijderde_scores": aantal})
            elif pad == "/crew/reset":
                opslag.reset()
                self._json(200, {"ok": True})
            elif pad == "/api/speler":
                sid = opslag.voeg_speler_toen(str(data.get("naam", "")))
                self._json(200, {"ok": True, "id": sid})
            else:
                self._json(404, {"fout": "Unknown route."})
        except ValueError as e:
            self._json(400, {"fout": str(e)})
        except Exception:
            self._json(500, {"fout": "Unexpected server error."})

    def log_message(self, fmt, *args):  # rustigere console
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {args[0] if args else ''}")


def main():
    parser = argparse.ArgumentParser(description="LAN-party leaderboard")
    parser.add_argument("--port", type=int, default=8321)
    parser.add_argument("--adres", default="0.0.0.0")
    parser.add_argument("--wachtwoord", help="Stel het crew-wachtwoord in (anders wordt er één gegenereerd)")
    args = parser.parse_args()

    wachtwoord = wachtwoord_inrichten(args.wachtwoord)
    server = ThreadingHTTPServer((args.adres, args.port), Handler)
    print(f"Leaderboard staat klaar op http://{args.adres}:{args.port}")
    print(f"  scherm:    http://<deze-pc>:{args.port}/")
    print(f"  registratie: http://<deze-pc>:{args.port}/registreer")
    print(f"  crew:      http://<deze-pc>:{args.port}/crew")
    print(f"Crew-wachtwoord: {wachtwoord}  (opgeslagen in config.json — niet delen)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Gestopt.")


if __name__ == "__main__":
    main()
