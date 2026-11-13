#!/usr/bin/env python3
"""Schakelt de arcade tussen de verticale Dell (DP-1) en de horizontale HP (DP-2) op GNOME Wayland.

HP aangesloten/aan  -> enkel de HP aan, horizontaal.
HP los/uit          -> enkel de Dell aan, verticaal.

xrandr werkt niet op Wayland, daarom praat dit script rechtstreeks met Mutter (de GNOME-
schermbeheerder) via D-Bus. Het blijft draaien en reageert op het MonitorsChanged-signaal,
zodat omschakelen ook werkt als de HP wordt in- of uitgeschakeld terwijl de arcade aanstaat.
"""
import subprocess
import sys
import time

from gi.repository import Gio, GLib

DELL_CONNECTOR = "DP-1"
HP_CONNECTOR = "DP-2"
# Mutter-rotatie: 0 = normaal, 1 = 90 graden, 3 = 270 graden.
# Staat het Dell-beeld ondersteboven, verander DELL_TRANSFORM dan van 3 naar 1.
DELL_TRANSFORM = 3
HP_TRANSFORM = 0
PREFERRED_RESOLUTION = (1920, 1080)
SCALE = 1.0

# Tijdelijk toepassen: bij 'persistent' toont GNOME een venster "Instellingen behouden?" en zet
# het na 20 seconden alles terug als niemand klikt. Het script past de opstelling bij elke
# login en schermwijziging toch opnieuw toe, dus opslaan is niet nodig.
APPLY_METHOD_TEMPORARY = 1
# Een aansluiting geeft vaak meerdere signalen kort na elkaar; wacht tot het rustig is.
SETTLE_DELAY_MS = 1500

# EmulationStation wordt bij het inloggen al gestart door dit opstartitem; bij een herstart
# gebruiken we hetzelfde item zodat het op exact dezelfde manier opstart.
RETROPIE_LAUNCHER = "/home/vives-arcade/.config/autostart/retropie.desktop"
FRONTEND_PROCESSES = ("retroarch", "emulationstation")

MUTTER_NAME = "org.gnome.Mutter.DisplayConfig"
MUTTER_PATH = "/org/gnome/Mutter/DisplayConfig"
APPLY_SIGNATURE = "(uua(iiduba(ssa{sv}))a{sv})"


def log(message):
    print(f"[display-switch] {message}", file=sys.stderr, flush=True)


class DisplayLayout:
    """Kiest en past de juiste schermopstelling toe via Mutter."""

    def __init__(self, mutter_proxy):
        self._mutter = mutter_proxy

    def apply_wanted_layout(self):
        """Past de gewenste opstelling toe. Geeft True terug als er iets veranderd is."""
        serial, monitors, logical_monitors, _ = self._current_state()
        connected = {monitor[0][0]: monitor for monitor in monitors}
        target = self._choose_target(connected)
        if target is None:
            log(f"Geen {HP_CONNECTOR} of {DELL_CONNECTOR} gevonden, niets te doen.")
            return False
        connector, transform = target
        if self._is_active(logical_monitors, connector, transform):
            return False
        mode_id = self._choose_mode(connected[connector])
        self._apply(serial, connector, mode_id, transform)
        log(f"Omgeschakeld naar {connector} (rotatie {transform}, modus {mode_id}).")
        return True

    def _current_state(self):
        result = self._mutter.call_sync("GetCurrentState", None, Gio.DBusCallFlags.NONE, -1, None)
        return result.unpack()

    @staticmethod
    def _choose_target(connected):
        if HP_CONNECTOR in connected:
            return HP_CONNECTOR, HP_TRANSFORM
        if DELL_CONNECTOR in connected:
            return DELL_CONNECTOR, DELL_TRANSFORM
        return None

    @staticmethod
    def _is_active(logical_monitors, connector, transform):
        if len(logical_monitors) != 1:
            return False
        logical = logical_monitors[0]
        active_connectors = [monitor[0] for monitor in logical[5]]
        return active_connectors == [connector] and logical[3] == transform

    @staticmethod
    def _choose_mode(monitor):
        modes = monitor[1]
        matching = [mode for mode in modes if (mode[1], mode[2]) == PREFERRED_RESOLUTION]
        if matching:
            return max(matching, key=lambda mode: mode[3])[0]
        preferred = [mode for mode in modes if mode[6].get("is-preferred")]
        return (preferred or modes)[0][0]

    def _apply(self, serial, connector, mode_id, transform):
        logical_monitor = (0, 0, SCALE, transform, True, [(connector, mode_id, {})])
        parameters = GLib.Variant(APPLY_SIGNATURE, (serial, APPLY_METHOD_TEMPORARY, [logical_monitor], {}))
        self._mutter.call_sync("ApplyMonitorsConfig", parameters, Gio.DBusCallFlags.NONE, -1, None)


class Frontend:
    """Herstart EmulationStation zodat het zich aanpast aan het nieuwe scherm."""

    @staticmethod
    def restart():
        for process in FRONTEND_PROCESSES:
            subprocess.run(["killall", "-q", process])
        time.sleep(1)
        subprocess.Popen(["gio", "launch", RETROPIE_LAUNCHER], start_new_session=True)
        log("EmulationStation herstart.")


class DisplaySwitcher:
    """Koppelt schermwijzigingen aan een nieuwe opstelling en een herstart van de frontend."""

    def __init__(self, layout, frontend):
        self._layout = layout
        self._frontend = frontend
        self._pending_check = None

    def start(self, mutter_proxy):
        self._switch_safely()
        mutter_proxy.connect("g-signal", self._on_signal)

    def _on_signal(self, _proxy, _sender, signal_name, _parameters):
        if signal_name != "MonitorsChanged":
            return
        if self._pending_check is not None:
            GLib.source_remove(self._pending_check)
        self._pending_check = GLib.timeout_add(SETTLE_DELAY_MS, self._on_settled)

    def _on_settled(self):
        self._pending_check = None
        if self._switch_safely():
            self._frontend.restart()
        return GLib.SOURCE_REMOVE

    def _switch_safely(self):
        try:
            return self._layout.apply_wanted_layout()
        except GLib.Error as error:
            log(f"Omschakelen mislukt: {error.message}")
            return False


def main():
    mutter = Gio.DBusProxy.new_for_bus_sync(
        Gio.BusType.SESSION, Gio.DBusProxyFlags.NONE, None, MUTTER_NAME, MUTTER_PATH, MUTTER_NAME, None)
    switcher = DisplaySwitcher(DisplayLayout(mutter), Frontend())
    switcher.start(mutter)
    GLib.MainLoop().run()


if __name__ == "__main__":
    main()
