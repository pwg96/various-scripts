#!/usr/bin/env python3

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# 
# Copyright (C) 2019 pwg96 (bodzioslaw aka pwg)
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
# 
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.
#
# kumiko.py - KDE5 wallpaper randomizer
# This script sets random wallpaper on every screen.
# This script is also executed by cronjob exclusively.
#
# USAGE:
# Put wallpapers you want to use under $HOME/.wallpapers and
# create crontab entry similar to this one: 
#
# */15 * * * * DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u "${LOGNAME}")/bus" python3 "${HOME}/scripts/kumiko.py"
#
# WARNING!
# THIS SCRIPT WORKS WITH KDE 5.13 AND LATER, OTHERWISE YOU WILL NEED
# TO LEAVE WIDGEDS UNLOCKED.

import dbus
import os
import mimetypes
import random

def get_wallpaper(path):

    wallpaper_list = []
    valid_mimetypes = ['image/jpg', 'image/jpeg', 'image/png']

    # get list of images from path catalog
    for file in os.listdir(path):
        mimetype = mimetypes.MimeTypes().guess_type(file)[0]
        if mimetype in valid_mimetypes:
            wallpaper_list.append(file)

    random_wallpaper = random.choice(wallpaper_list)
    return os.path.join(path, random_wallpaper)

def set_wallpaper(wallpaper):

    # wallpaper script for dbus
    dbus_script = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "file://%s")
    }"""

    # dbus session
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')

    plasma.evaluateScript(dbus_script % wallpaper)

if __name__ == "__main__":
    # variables
    path = os.environ['HOME'] + '/.wallpapers'

    chosen_wallpaper = get_wallpaper(path)
    set_wallpaper(chosen_wallpaper)
