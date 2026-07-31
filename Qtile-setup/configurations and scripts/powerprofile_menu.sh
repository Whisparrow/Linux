#!/bin/bash

options="Performance\nBalanced\nPower Saver"
chosen=$(echo -e "$options" | rofi -dmenu -p "Power Profile")

case "$chosen" in
    "Power Saver")
        powerprofilesctl set power-saver
        ;;
    "Balanced")
        powerprofilesctl set balanced
        ;;
    "Performance")
        powerprofilesctl set performance
        ;;
esac
