#!/bin/bash

echo "Installing KioskDE..."

sudo mkdir -p /usr/local/bin
sudo mkdir -p /usr/share/xsessions
sudo mkdir -p /usr/share/kioskde/assets
sudo mkdir -p /etc/kioskde

sudo cp bin/* /usr/local/bin/
sudo chmod +x /usr/local/bin/kiosk-*

sudo cp sessions/kioskde.desktop /usr/share/xsessions/
sudo cp assets/* /usr/share/kioskde/assets/

echo "KioskDE installed."
echo "Log out and select 'KioskDE' session."
