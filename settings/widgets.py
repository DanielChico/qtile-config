import os

from libqtile import qtile, widget
from qtile_extras import widget

from .colors import colors
from .config import group_fontsize, terminal, text_fontsize, side_fontsize, group_font

widget_defaults = dict(
    font="Ubuntu Bold", fontsize=10, padding=2, background=colors["background"]
)
extension_defaults = widget_defaults.copy()


def separator():
    return widget.Sep(
        linewidth=0,
        padding=6,
        foreground=colors["light_grey"],
        background=colors["background"],
    )


def line_separator():
    return widget.TextBox(
        text="|",
        font="Ubuntu Mono",
        background=colors["background"],
        foreground="474747",
        padding=2,
        fontsize=25,
    )


widgets_list = [
    separator(),
    separator(),
    widget.Image(
        filename="~/.config/qtile/icons/linux_archlinux_icon.svg",
        scale="False",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=10,
    ),
    separator(),
    separator(),
    widget.Sep(
        linewidth=2,
        padding=0,
        size_percent=80,
        foreground="474747",
        background=colors["background"],
    ),
    widget.GroupBox(
        font=group_font,
        fontsize=group_fontsize,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=10,
        borderwidth=3,
        active=colors["light_grey"],
        inactive=colors["light_blue"],
        rounded=False,
        highlight_color=colors["dark"],
        highlight_method="line",
        this_current_screen_border=colors["light_blue"],
        this_screen_border=colors["light_green"],
        other_current_screen_border=colors["light_blue"],
        other_screen_border=colors["light_green"],
        foreground=colors["light_grey"],
        background=colors["background"],
        # "#232136"
    ),
    line_separator(),
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
        fontsize=side_fontsize,
    ),
    line_separator(),
    widget.WindowName(
        foreground=colors["light_blue"],
        background=colors["background"],
        padding=0,
        fontsize=side_fontsize,
    ),
    widget.Systray(
        background=colors["background"],
        padding=5,
        icon_size=20,
        fontsize=text_fontsize,
    ),
    separator(),
    line_separator(),
    widget.Net(
        #    interface = "enp6s0",
        format="  {down}   {up}",
        foreground=colors["light_red"],
        background=colors["background"],
        padding=5,
        fontsize=text_fontsize,
    ),
    separator(),
    line_separator(),
    separator(),
    widget.TextBox(
        text="",
        font="Ubuntu Mono",
        background=colors["background"],
        foreground=colors["dark_gray"],
        padding=4,
        fontsize=20,
    ),
    widget.CPU(
        background=colors["background"],
        foreground=colors["dark_gray"],
        format="{load_percent}%",
        fontsize=text_fontsize,
        padding=5,
    ),
    separator(),
    line_separator(),
    separator(),
    widget.TextBox(
        text="󰍛",
        font="Ubuntu Mono",
        background=colors["background"],
        foreground=colors["light_purple"],
        padding=4,
        fontsize=20,
    ),
    widget.Memory(
        foreground=colors["light_purple"],
        background=colors["background"],
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        fmt="{}",
        padding=5,
        fontsize=text_fontsize,
    ),
    separator(),
    line_separator(),
    separator(),
    widget.Volume(
        theme_path="~/.config/qtile/icons/volume",
        background=colors["background"],
        fontsize=text_fontsize,
        emoji=True,
    ),
    widget.PulseVolume(
        foreground=colors["mate_purple"],
        background=colors["background"],
        fmt="{}",
        padding=0,
        fontsize=text_fontsize,
    ),
    separator(),
    line_separator(),
    widget.BatteryIcon(
        theme_path='~/.config/qtile/icons/battery',
        background=colors["background"],
        scale=1,
    ),
    widget.Battery(
        foreground=colors["mate_purple"],
        background=colors["background"],
        notify_below=20,
        format="{percent:2.0%}",
        fontsize=text_fontsize,
    ),
    separator(),
    line_separator(),
    widget.Clock(
        foreground=colors["light_blue"],
        background=colors["background"],
        format="    %B %d - %H:%M ",
        fontsize=text_fontsize,
    ),
    separator(),
]
