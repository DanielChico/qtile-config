#!/usr/bin/env bash 

# festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
# /usr/bin/emacs --daemon &
# conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc
volumeicon &
nm-applet &
blueman-applet &
# Enable natural scrolling
xinput set-prop "ELAN0709:00 04F3:31BF Touchpad" "libinput Natural Scrolling Enabled" 1 &
#Enable tapping
xinput set-prop "ELAN0709:00 04F3:31BF Touchpad" "libinput Tapping Enabled" 1

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
