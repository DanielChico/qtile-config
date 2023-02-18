from libqtile import bar
from libqtile.config import Screen

from .config import background_wallpaper, bar_size
from .widgets import widgets_list

screens = [
    Screen(
        wallpaper=background_wallpaper,
        wallpaper_mode="fill",
        top=bar.Bar(widgets=widgets_list, opacity=1.0, size=bar_size),
    )
    # Screen(
    #     wallpaper=background_wallpaper,
    #     wallpaper_mode="fill",
    #     top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
    # Screen(
    #     wallpaper=background_wallpaper,
    #     wallpaper_mode="fill",
    #     top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))
]
