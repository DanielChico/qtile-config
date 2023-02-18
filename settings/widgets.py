import os

from libqtile import qtile, widget
from qtile_extras import widget

from .colors import colors
from .config import group_fontsize, terminal, text_fontsize

widget_defaults = dict(
    font="Ubuntu Bold", fontsize=10, padding=2, background=colors["light_grey"]
)
extension_defaults = widget_defaults.copy()


def separator():
    return widget.Sep(
        linewidth=0,
        padding=6,
        foreground=colors["light_grey"],
        background=colors["background"],
    )


widgets_list = [
    separator(),
    widget.Image(
        filename="~/.config/qtile/icons/python-white.png",
        scale="False",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
    ),
    separator(),
    widget.GroupBox(
        font="Ubuntu Bold",
        fontsize=group_fontsize,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=3,
        borderwidth=3,
        active=colors["light_grey"],
        inactive=colors["purple"],
        rounded=False,
        highlight_color=colors["dark"],
        highlight_method="line",
        this_current_screen_border=colors["light_blue"],
        this_screen_border=colors["light_green"],
        other_current_screen_border=colors["light_blue"],
        other_screen_border=colors["light_green"],
        foreground=colors["light_grey"],
        background=colors["background"],
    ),
    widget.TextBox(
        text="|",
        font="Ubuntu Mono",
        background=colors["background"],
        foreground="474747",
        padding=2,
        fontsize=text_fontsize,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        foreground=colors["light_grey"],
        background=colors["background"],
        padding=0,
        scale=0.7,
    ),
    widget.CurrentLayout(
        foreground=colors["light_grey"],
        background=colors["background"],
        padding=5,
        fontsize=group_fontsize,
    ),
    widget.TextBox(
        text="|",
        font="Ubuntu Mono",
        background=colors["background"],
        foreground="474747",
        padding=2,
        fontsize=text_fontsize,
    ),
    widget.WindowName(
        foreground=colors["light_blue"],
        background=colors["background"],
        padding=0,
        fontsize=group_fontsize,
    ),
    widget.Systray(background=colors["background"], padding=5, fontsize=text_fontsize),
    separator(),
    widget.Net(
        #    interface = "enp6s0",
        format="Net: {down} ↓↑ {up}",
        foreground=colors["light_red"],
        background=colors["background"],
        padding=5,
        fontsize=text_fontsize,
    ),
    separator(),
    widget.Memory(
        foreground=colors["light_purple"],
        background=colors["background"],
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        fmt="Mem: {}",
        padding=5,
        fontsize=text_fontsize,
    ),
    separator(),
    widget.Volume(
        foreground=colors["purple"],
        background=colors["background"],
        fmt="Vol: {}",
        padding=5,
        fontsize=text_fontsize,
    ),
    separator(),
    widget.Battery(
        foreground=colors["light_blue"],
        background=colors["background"],
        notify_below=20,
        format="{percent:2.0%}",
        fontsize=text_fontsize,
    ),
    widget.UPowerWidget(background=colors["background"], fontsize=text_fontsize),
    separator(),
    widget.Clock(
        foreground=colors["light_blue"],
        background=colors["background"],
        format="%A, %B %d - %H:%M ",
        fontsize=text_fontsize,
    ),
    separator(),
]
