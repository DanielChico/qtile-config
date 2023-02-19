import subprocess

from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger

from .config import background_wallpaper, bar_size
from .widgets import widgets_list

screens = [
    Screen(
        wallpaper=background_wallpaper,
        wallpaper_mode="fill",
        top=bar.Bar(widgets=widgets_list, opacity=1.0, size=bar_size),
    )
]
CONNECT_LAPTOP_MONITOR = "xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off"
DISCONNECT_LAPTOP_MONITOR = "xrandr --output eDP-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off"
xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors == 1:
    subprocess.run(
        CONNECT_LAPTOP_MONITOR,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

if connected_monitors > 1:
    subprocess.run(
        DISCONNECT_LAPTOP_MONITOR,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
