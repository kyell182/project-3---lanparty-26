// LAN Admin: login is al gebeurd (server toont deze pagina pas na aanmelding).
let spelerMap = {}; // id -> naam

function meld(t, ok) {
  const m = document.getElementById("melding");
  m.textContent = t;
  m.className = ok ? "ok" : "fout";
  setTimeout(() => (m.className = ""), 6000);
}

async function api(pad, body) {
  const r = await fetch(pad, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body || {}),
  });
  return r.json();
}

async function ververs() {
  const [d, s, r] = await Promise.all([
    fetch("/api/data", { cache: "no-store" }).then(x => x.json()),
    fetch("/crew/spelers").then(x => x.ok ? x.json() : null),
    fetch("/crew/recent").then(x => x.ok ? x.json() : null),
  ]);
  tekenGames(d.games);
  if (s) tekenSpelers(s.spelers);
  if (r) tekenRecent(r.recent);
}

function tekenSpelers(spelers) {
  const tb = document.getElementById("spelers-body");
  document.getElementById("spelers-leeg").style.display = spelers.length ? "none" : "";
  tb.innerHTML = spelers.map(s => `
    <tr>
      <td>${escapeHtml(s.naam)}</td>
      <td style="text-align:right">
        <button class="klein gevaar" onclick="spelerVerwijder('${s.id}')">Remove</button>
      </td>
    </tr>`).join("");
  // Vul de Player-dropdown (score-invoer)
  const sel = document.getElementById("speler");
  const huidig = sel.value;
  spelerMap = Object.fromEntries(spelers.map(s => [s.id, s.naam]));
  sel.innerHTML = spelers.length
    ? spelers.map(s => `<option value="${s.id}">${escapeHtml(s.naam)}</option>`).join("")
    : `<option value="">— add a player below —</option>`;
  if (huidig && spelers.some(s => s.id === huidig)) sel.value = huidig;
}

function tekenRecent(recent) {
  const tb = document.getElementById("recent-body");
  document.getElementById("recent-leeg").style.display = recent.length ? "none" : "";
  tb.innerHTML = recent.map(s => `
    <tr>
      <td class="klein">${escapeHtml(fkort(s.ingevuld_op))}</td>
      <td>${escapeHtml(s.speler_naam)}</td>
      <td>${escapeHtml(s.game_naam)}</td>
      <td class="hist-waarde">${Number(s.waarde).toLocaleString("en-GB")}</td>
      <td style="text-align:right">
        <button class="klein gevaar" onclick="undoScore('${s.id}', '${escapeHtml(s.speler_naam)}', '${escapeHtml(s.game_naam)}')">Undo</button>
      </td>
    </tr>`).join("");
}

function fkort(iso) {
  // "2026-10-22T18:04:00" -> "18:04"
  const m = String(iso).match(/T(\d{2}:\d{2}:\d{2})/);
  return m ? m[1] : iso;
}

function tekenGames(games) {
  const tb = document.getElementById("games-body");
  document.getElementById("games-leeg").style.display = games.length ? "none" : "";
  const select = document.getElementById("game");
  const huidig = select.value;
  select.innerHTML = games.length
    ? games.map(g => `<option value="${g.id}">${escapeHtml(g.naam)}</option>`).join("")
    : `<option value="">— add a game below —</option>`;
  if (huidig && games.some(g => g.id === huidig)) select.value = huidig;
  tb.innerHTML = games.length
    ? games.map(g => `<tr><td>${escapeHtml(g.naam)}</td>
        <td style="text-align:right"><button class="klein gevaar" onclick="gameVerwijder('${g.id}')">Remove</button></td></tr>`).join("")
    : `<tr><td colspan="2" class="klein">No games yet.</td></tr>`;
}

async function spelerVerwijder(id) {
  const naam = spelerMap[id];
  if (!confirm(`Remove player "${naam}"? All their scores are removed too.`)) return;
  const d = await api("/crew/speler/verwijder", { id });
  meld(d.ok ? `Removed: ${naam} (${d.verwijderde_scores} scores).` : d.fout, d.ok);
}

async function gameVerwijder(id) {
  if (!confirm("Remove this game? All its scores are removed too.")) return;
  const d = await api("/crew/game/verwijder", { id });
  meld(d.ok ? "Game removed." : d.fout, d.ok);
}

async function undoScore(id, speler, game) {
  if (!confirm(`Undo score of ${speler} in ${game}? The score is subtracted and the history entry removed.`)) return;
  const d = await api("/crew/score/verwijder", { id });
  meld(d.ok ? "Score removed (undo)." : d.fout, d.ok);
}

document.getElementById("verzenden").onclick = async () => {
  const spelerId = document.getElementById("speler").value;
  const waarde = parseFloat(document.getElementById("waarde").value);
  if (!spelerId) { meld("Add or pick a player first.", false); return; }
  if (isNaN(waarde) || waarde < 0 || waarde > 100) {
    meld("Score must be between 0 and 100.", false); return;
  }
  const d = await api("/crew/score", {
    game_id: document.getElementById("game").value,
    naam: spelerMap[spelerId],
    waarde,
  });
  if (d.ok) {
    document.getElementById("waarde").value = "";
    document.getElementById("waarde").focus();
    meld("Score added.");
  } else meld(d.fout, false);
};

document.getElementById("speler-toevoegen").onclick = async () => {
  const d = await api("/crew/speler", { naam: document.getElementById("nieuwe-speler").value });
  if (d.ok) {
    document.getElementById("nieuwe-speler").value = "";
    document.getElementById("nieuwe-speler").focus();
    meld("Player added.");
  } else meld(d.fout, false);
};

document.getElementById("game-toevoegen").onclick = async () => {
  const d = await api("/crew/game", { naam: document.getElementById("nieuwe-game").value });
  if (d.ok) {
    document.getElementById("nieuwe-game").value = "";
    document.getElementById("nieuwe-game").focus();
    meld("Game added.");
  } else meld(d.fout, false);
};

document.getElementById("reset").onclick = async () => {
  if (!confirm("Wipe ALL data? This cannot be undone.")) return;
  const d = await api("/crew/reset", {});
  meld(d.ok ? "All data wiped." : d.fout, d.ok);
};

document.getElementById("afmelden").onclick = async () => {
  await api("/crew/afmelden", {});
  location.href = "/crew";
};

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

ververs();
setInterval(ververs, 5000);
