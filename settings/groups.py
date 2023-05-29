from libqtile.config import Group
from libqtile.dgroups import simple_key_binder

from .config import mod

groups = [
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("󰉋", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("󰋋", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("", layout="floating"),
]

dgroups_key_binder = simple_key_binder(mod)
