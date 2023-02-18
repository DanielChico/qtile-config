# -*- coding: utf-8 -*-
import os
import socket
import subprocess

from libqtile import bar, hook, layout
from libqtile.config import Screen

from settings.config import (
    browser,
    chat,
    code_editor,
    filemanager,
    group_fontsize,
    mod,
    terminal,
    text_fontsize,
)
from settings.groups import dgroups_key_binder, groups
from settings.keys import keys
from settings.layout import (
    auto_fullscreen,
    floating_layout,
    focus_on_window_activation,
    layouts,
    reconfigure_screens,
)
from settings.mouse import (
    bring_front_click,
    cursor_warp,
    dgroups_app_rules,
    follow_mouse_focus,
    mouse,
)
from settings.screens import screens
from settings.widgets import extension_defaults, widget_defaults, widgets_list

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


# def window_to_prev_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i - 1].name)


# def window_to_next_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i + 1].name)


# def window_to_previous_screen(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     if i != 0:
#         group = qtile.screens[i - 1].group.name
#         qtile.current_window.togroup(group)


# def window_to_next_screen(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     if i + 1 != len(qtile.screens):
#         group = qtile.screens[i + 1].group.name
#         qtile.current_window.togroup(group)


# def switch_screens(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     group = qtile.screens[i - 1].group
#     qtile.current_screen.set_group(group)


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
