#!/bin/bash

echo "Uninstalling KioskDE..."

# remove binaries
sudo rm -f /usr/local/bin/kiosk-session.sh
sudo rm -f /usr/local/bin/kiosk-launch.sh
sudo rm -f /usr/local/bin/kiosk-admin.sh
sudo rm -f /usr/local/bin/kiosk-init-ui.py

# remove session entry
sudo rm -f /usr/share/xsessions/kioskde.desktop

# remove assets
sudo rm -rf /usr/share/kioskde

# remove system config
sudo rm -rf /etc/kioskde

echo "KioskDE removed."
echo "You may want to reboot."
