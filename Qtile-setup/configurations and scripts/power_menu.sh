#!/bin/bash
selected=$(printf "Lock\nLogout\nSleep\nReboot\nShutdown" | rofi -dmenu -p "Power Menu")

case "$selected" in
    "Lock") ~/.config/qtile/scripts/lock.sh ;;
    "Logout") pkill -u $USER ;;
    "Sleep") systemctl suspend ;;
    "Reboot") systemctl reboot ;;
    "Shutdown") systemctl poweroff ;;
esac
