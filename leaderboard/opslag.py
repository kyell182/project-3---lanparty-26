"""Datalaag van de leaderboard: JSON-bestand, threadveilig, offline.

Geen externe afhankelijkheden (Python stdlib). Alle persoonsgegevens blijven
lokaal; in de data staan enkel pseudoniemen (zie README.md).
"""

import json
import os
import re
import threading
import uuid
from datetime import datetime

_DATA_PAD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
_DATA_BESTAND = os.path.join(_DATA_PAD, "leaderboard.json")

# Toegestane karakters voor een pseudoniem: letters, cijfers, koppelteken,
# laag streeppunt, punt, komma, spatie, haakjes, uitroepteken, vraagteken.
_NAAM_PAT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 .,_\-()!?éèêëàäöü]{1,39}$")

_lek = threading.Lock()


def _leeg() -> dict:
    return {"games": {}, "spelers": {}, "scores": []}


def _laad() -> dict:
    """Laad de data; terugval op een lege structuur als het bestand ontbreekt."""
    if not os.path.exists(_DATA_BESTAND):
        return _leeg()
    with open(_DATA_BESTAND, encoding="utf-8") as f:
        data = json.load(f)
    # Structuur compleet houden na handmatige wijzigingen.
    data.setdefault("games", {})
    data.setdefault("spelers", {})
    data.setdefault("scores", [])
    return data


def _sluit(data: dict) -> None:
    """Atomaire schrijf: eerst naar een tijdelijk bestand, daarna omwisselen."""
    os.makedirs(_DATA_PAD, exist_ok=True)
    tijdelijk = _DATA_BESTAND + ".tmp"
    with open(tijdelijk, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tijdelijk, _DATA_BESTAND)


def _nieuw_id() -> str:
    return uuid.uuid4().hex[:10]


def valideer_naam(naam: str) -> str:
    """Controleer een pseudoniem; gooi WaardeFout bij ongeldige invoer."""
    naam = (naam or "").strip()
    if not _NAAM_PAT.match(naam):
        raise ValueError(
            "Invalid name: 2 to 40 characters, start with a letter or digit, "
            "letters, digits and .,_-()? only"
        )
    return naam


# ------------------------------------------------------------------ games

def games() -> list:
    """Alle games met hun volgorde (vaste volgorde op het scherm)."""
    with _lek:
        data = _laad()
        return [
            {"id": gid, "naam": g["naam"], "eenheid": g.get("eenheid", "punten")}
            for gid, g in data["games"].items()
        ]


def nieuwe_game(naam: str) -> str:
    """Voeg een game toe (id terug). Namen zijn uniek per leaderboard."""
    naam = (naam or "").strip()
    if not naam or len(naam) > 60:
        raise ValueError("Game name: 1 to 60 characters.")
    with _lek:
        data = _laad()
        bestaand = [g for g in data["games"].values() if g["naam"].lower() == naam.lower()]
        if bestaand:
            raise ValueError(f"Game already exists: {naam}")
        gid = _nieuw_id()
        data["games"][gid] = {"naam": naam, "eenheid": "punten", "volgorde": len(data["games"]) + 1}
        _sluit(data)
        return gid


def verwijder_game(gid: str) -> bool:
    """Verwijder een game én alle scores bij die game (herroepbaar via back-up)."""
    with _lek:
        data = _laad()
        if gid not in data["games"]:
            return False
        del data["games"][gid]
        data["scores"] = [s for s in data["scores"] if s["game_id"] != gid]
        _sluit(data)
        return True


# --------------------------------------------------------------- spelers

def spelers() -> list:
    """Alle geregistreerde pseudoniemen."""
    with _lek:
        data = _laad()
        return [
            {"id": sid, "naam": s["naam"]}
            for sid, s in data["spelers"].items()
        ]


def voeg_speler_toen(naam: str) -> str:
    """Registreer een pseudoniem; identieke naam levert dezelfde speler op."""
    naam = valideer_naam(naam)
    with _lek:
        data = _laad()
        voor_schrijf = {s["naam"].lower(): sid for sid, s in data["spelers"].items()}
        if naam.lower() in voor_schrijf:
            return voor_schrijf[naam.lower()]
        sid = _nieuw_id()
        data["spelers"][sid] = {"naam": naam}
        _sluit(data)
        return sid


def verwijder_speler(sid: str) -> int:
    """Verwijder een speler én al haar/zijn scores. Geeft het aantal
    verwijderde scores terug (0 = speler bestaat niet)."""
    with _lek:
        data = _laad()
        if sid not in data["spelers"]:
            return 0
        del data["spelers"][sid]
        voor = len(data["scores"])
        data["scores"] = [s for s in data["scores"] if s["speler_id"] != sid]
        _sluit(data)
        return voor - len(data["scores"])


# ---------------------------------------------------------------- scores

def bewaar_score(gid: str, pseudoniem: str, waarde: float) -> dict:
    """Bewaar één score; onbekend pseudoniem wordt automatisch geregistreerd.
    'hoger is beter' voor alle games (zie README §normering)."""
    if gid not in _games_set():
        raise ValueError("Unknown game.")
    try:
        waarde = float(waarde)
    except (TypeError, ValueError):
        raise ValueError("Score must be a number.")
    if waarde < 0 or waarde > 100:
        raise ValueError("Score must be between 0 and 100.")

    sid = voeg_speler_toen(pseudoniem)
    meting = {
        "id": _nieuw_id(),
        "game_id": gid,
        "speler_id": sid,
        "waarde": waarde,
        "ingevuld_op": datetime.now().isoformat(timespec="seconds"),
    }
    with _lek:
        data = _laad()
        data["scores"].append(meting)
        _sluit(data)
    return meting


def verwijder_score(meting_id: str) -> bool:
    """Herroep één (mogelijk per ongeluk ingevoerde) score."""
    with _lek:
        data = _laad()
        voor = len(data["scores"])
        data["scores"] = [s for s in data["scores"] if s["id"] != meting_id]
        if len(data["scores"]) == voor:
            return False
        _sluit(data)
        return True


def recent_scores(limiet: int = 20) -> list:
    """De laatste ingevoerde scores, oudste naar nieuwste, voor de crew-pagina."""
    with _lek:
        data = _laad()
        scores = list(data["scores"])[-limiet:]
    games = {gid: g["naam"] for gid, g in data["games"].items()}
    namen = {sid: s["naam"] for sid, s in data["spelers"].items()}
    return [
        {
            **s,
            "game_naam": games.get(s["game_id"], "?"),
            "speler_naam": namen.get(s["speler_id"], "?"),
        }
        for s in scores
    ]


def _games_set() -> set:
    with _lek:
        return set(_laad()["games"].keys())


# ------------------------------------------------------- ranglijsten

def top_per_game(n: int = 10) -> list:
    """Per game: top-n spelers op som van hun ingevoerde 0-100 scores."""
    with _lek:
        data = _laad()
    stat = _scorestat(data)
    namen = {sid: s["naam"] for sid, s in data["spelers"].items()}
    resultaat = []
    for gid, g in data["games"].items():
        rijen = [
            {"naam": namen.get(sid, "?"), "waarde": cell["som"]}
            for sid, cell in stat.get(gid, {}).items()
        ]
        rijen.sort(key=lambda x: -x["waarde"])
        top = [
            {**t, "genormaliseerd": round(t["waarde"], 1)}
            for t in rijen[:n]
        ]
        resultaat.append({"id": gid, "naam": g["naam"], "eenheid": "score", "top": top})
    # Volgorde van de games zoals die zijn toegevoegd.
    resultaat.sort(key=lambda r: data["games"][r["id"]].get("volgorde", 0))
    return resultaat


def _scorestat(data: dict) -> dict:
    """Statistieken per (game, speler): som, hoogste enkele score en aantal.

    Elke ingevoerde score is al een 0-100 waarde (de crew toekent die zelf).
    Geeft {game_id: {speler_id: {"som": float, "hoogste": float, "aantal": int}}}.
    """
    stat = {}
    for s in data["scores"]:
        cell = stat.setdefault(s["game_id"], {}).setdefault(
            s["speler_id"], {"som": 0.0, "hoogste": 0.0, "aantal": 0}
        )
        w = s["waarde"]
        cell["som"] += w
        cell["hoogste"] = max(cell["hoogste"], w)
        cell["aantal"] += 1
    return stat


def _beste_game(stat: dict, speler_id: str) -> tuple | None:
    """Beste game van een speler: de game met de hoogste enkele 0-100 score.
    Tie-break: de game waarin de speler het meest speelde (aantal scores).

    Geeft (game_id, hoogste_score) of None als er nog geen scores zijn.
    """
    best_id, best_score, best_aantal = None, -1.0, -1
    for gid, per_speler in stat.items():
        if speler_id not in per_speler:
            continue
        score = per_speler[speler_id]["hoogste"]
        aantal = per_speler[speler_id]["aantal"]
        if score > best_score + 1e-9 or (abs(score - best_score) <= 1e-9 and aantal > best_aantal):
            best_id, best_score, best_aantal = gid, score, aantal
    if best_id is None:
        return None
    return best_id, best_score


def totaalstand(n: int = 20) -> list:
    """Globale totaalstand: som van alle ingevoerde 0-100 scores per speler
    (elke gespeelde game/sessie telt mee in het totaal).

    Elke rij bevat 'naam', 'totaal' (som van alle scores), 'beste_game' (naam
    van de game met de speler's hoogste enkele score) en 'beste_waarde' (die
    0-100 score)."""
    with _lek:
        data = _laad()
    stat = _scorestat(data)
    namen = {sid: s["naam"] for sid, s in data["spelers"].items()}
    game_namen = {gid: g["naam"] for gid, g in data["games"].items()}
    totalen = {}
    for per_speler in stat.values():
        for sid, cell in per_speler.items():
            totalen[sid] = totalen.get(sid, 0.0) + cell["som"]
    rijen = []
    for sid, t in totalen.items():
        rij = {"naam": namen.get(sid, "?"), "totaal": round(t, 1)}
        beste = _beste_game(stat, sid)
        if beste:
            rid, score = beste
            rij["beste_game"] = game_namen.get(rid, "?")
            rij["beste_waarde"] = round(score, 1)
        else:
            rij["beste_game"] = ""
            rij["beste_waarde"] = 0.0
        rijen.append(rij)
    rijen.sort(key=lambda x: -x["totaal"])
    return rijen[:n]


def reset() -> None:
    """Verwijder alle data (games, spelers, scores) — terug naar een leeg systeem."""
    with _lek:
        _sluit(_leeg())
