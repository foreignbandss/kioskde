#!/usr/bin/env python3

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ASSETS = "/usr/share/kioskde/assets"
CFG = "/etc/kioskde"

class Installer(Gtk.Window):
    def __init__(self):
        super().__init__(title="KioskDE Setup")
        self.set_default_size(900, 600)
        self.set_position(Gtk.WindowPosition.CENTER)

        overlay = Gtk.Overlay()
        self.add(overlay)

        bg = Gtk.Image.new_from_file(f"{ASSETS}/setupbg.png")
        overlay.add(bg)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)

        logo = Gtk.Image.new_from_file(f"{ASSETS}/logo1.png")
        box.pack_start(logo, False, False, 10)

        self.pin = Gtk.Entry()
        self.pin.set_placeholder_text("Set Admin PIN")
        self.pin.set_visibility(False)
        box.pack_start(self.pin, False, False, 5)

        self.mode = Gtk.ComboBoxText()
        self.mode.append_text("web")
        self.mode.append_text("local")
        self.mode.set_active(0)
        box.pack_start(self.mode, False, False, 5)

        self.target = Gtk.Entry()
        self.target.set_placeholder_text("URL or App")
        box.pack_start(self.target, False, False, 5)

        btn = Gtk.Button(label="Install KioskDE")
        btn.connect("clicked", self.finish)
        box.pack_start(btn, False, False, 10)

        overlay.add_overlay(box)

    def finish(self, _):
        os.makedirs(CFG, exist_ok=True)

        open(f"{CFG}/pin","w").write(self.pin.get_text())
        open(f"{CFG}/mode","w").write(self.mode.get_active_text())
        open(f"{CFG}/target","w").write(self.target.get_text())
        open(f"{CFG}/initialized","w").write("1")

        Gtk.main_quit()

win = Installer()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
