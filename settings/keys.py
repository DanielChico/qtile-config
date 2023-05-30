from libqtile import extension
from libqtile.config import Key
from libqtile.lazy import lazy

from .colors import colors
from .config import bar_size, browser, chat, code_editor, filemanager, mod, terminal

keys = [
    # The essentials
    Key(
        [mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launches My Terminal",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("dm-run"),
        desc="Run Launcher",
    ),
    Key(
        [mod],
        "b",
        lazy.spawn(browser),
        desc="google-chrome",
    ),
    Key(
        [mod],
        "c",
        lazy.spawn(code_editor),
        desc="vsCode",
    ),
    Key(
        [mod],
        "t",
        lazy.spawn(chat),
        desc="telegram",
    ),
    Key(
        [mod],
        "e",
        lazy.spawn(filemanager),
        desc="filemanager",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%"),
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-"),
    ),
    Key(
        [mod],
        "s",
        lazy.spawn(
            "scrot Pictures/Screenshots/Screenshot_from_%Y-%m-%d_%H-%M-%S.png -e 'xclip -selection clipboard -t image/png -i $f'"
),
# Pictures/Screenshots/Screenshot\ from\ %Y-%m-%d\ %H-%M-%S.png
    ),  # Screenshot
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(
            "scrot -s Pictures/Screenshots/Screenshot_from_%Y-%m-%d_%H-%M-%S.png -e 'xclip -selection clipboard -t image/png -i $f'"
        ),
    ),
    Key(
        [mod, "shift"],
        "Tab",
        lazy.next_layout(),
        desc="Toggle through layouts",
    ),
    Key(
        [mod, "shift"],
        "c",
        lazy.window.kill(),
        desc="Kill active window",
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.restart(),
        desc="Restart Qtile",
    ),
    Key(
        [mod, "shift"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    Key(
        ["control", "shift"],
        "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Doom Emacs",
    ),
    # Window controls
    Key(
        [mod],
        "j",
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key(
        [mod],
        "k",
        lazy.layout.up(),
        desc="Move focus up in current stack pane",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.reset(),
        desc="normalize window size ratios",
    ),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="toggle floating",
    ),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen",
    ),
    # Stack controls
    Key(
        [mod],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod],
        "p",
        lazy.run_extension(
            extension.DmenuRun(
                dmenu_prompt=">",
                dmenu_font="JetBrains Font",
                background=colors["background"],
                foreground=colors["light_blue"],
                selected_background=colors["dark"],
                selected_foreground=colors["light_grey"],
                dmenu_height=bar_size,  # Only supported by some dmenu forks
                dmenu_lines=10,
            )
        ),
    ),
]
