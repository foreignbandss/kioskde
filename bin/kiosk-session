#!/bin/bash

openbox &

sleep 1

if [ ! -f /etc/kioskde/initialized ]; then
    /usr/local/bin/kiosk-init-ui
fi

MODE=$(cat /etc/kioskde/mode)
TARGET=$(cat /etc/kioskde/target)

if [ "$MODE" = "web" ]; then
    firefox --kiosk "$TARGET"
else
    exec "$TARGET"
fi
