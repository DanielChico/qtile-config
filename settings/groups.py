from libqtile.config import Group
from libqtile.dgroups import simple_key_binder

from .config import mod

groups = [
    Group("WWW", layout="monadtall"),
    Group("DEV", layout="monadtall"),
    Group("SYS", layout="monadtall"),
    Group("SYS", layout="monadtall"),
    Group("DOC", layout="monadtall"),
    Group("VBOX", layout="monadtall"),
    Group("CHAT", layout="monadtall"),
    Group("MUS", layout="monadtall"),
    Group("VID", layout="monadtall"),
    Group("GFX", layout="floating"),
]

dgroups_key_binder = simple_key_binder(mod)
