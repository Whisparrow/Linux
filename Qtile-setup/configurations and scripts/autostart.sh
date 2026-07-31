#!/bin/sh

# Set the background wallpaper
feh --bg-fill "/home/aster/Pictures/wall_secondary.png" &

# Start Picom using your new dedicated config file
picom --config ~/.config/picom/picom.conf &

# Start the Polkit authentication agent for GUI password prompts
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# XFCE screen Startup
xfce4-screensaver &
xss-lock -- xfce4-screensaver-command --lock

# Set power profile to Balanced on startup
powerprofilesctl set balanced &

# Start XFCE notification manager
/usr/lib/xfce4/notifyd/xfce4-notifyd &

# Clear the old clipboard history file on boot for privacy
rm -f ~/.clipboard_history

# Clipboard background tracking loop (Ignores mouse highlights completely)
while true; do
    xclip -selection clipboard -o 2>/dev/null | tr '\n' ' ' >> ~/.clipboard_history
    echo '' >> ~/.clipboard_history
    awk '!awk_built_in_duplicate_check[$0]++' ~/.clipboard_history | tail -n 50 > ~/.clipboard_history.tmp
    mv ~/.clipboard_history.tmp ~/.clipboard_history
    xclip -selection clipboard -o -f 2>/dev/null
    sleep 1
done &
