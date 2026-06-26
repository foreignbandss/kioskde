#!/bin/bash

read -s -p "PIN: " pin
echo ""

REAL_PIN=$(cat /etc/kioskde/pin)

if [ "$pin" != "$REAL_PIN" ]; then
    echo "Denied"
    exit 1
fi

echo "KioskDE Admin"
echo "1) Change URL"
echo "2) Change Mode"

read -p "> " opt

case $opt in
    1)
        read -p "URL: " url
        echo "$url" > /etc/kioskde/target
        ;;
    2)
        read -p "Mode (web/local): " mode
        echo "$mode" > /etc/kioskde/mode
        ;;
esac
