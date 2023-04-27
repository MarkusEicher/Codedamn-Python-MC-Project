import json
from os import path
import winsound
from win10toast import ToastNotifier
from time import sleep

toaster = ToastNotifier()

# assets
SUN_VALLEY_THEME = path.join("sunvalley", "sv.tcl")
APP_ICO = path.join("assets", "app.ico") 
COFFE_ICO = path.join("assets", "coffee.ico")
DOLPHIN_WAV = path.join("assets", "dolphin.wav")

JSDTA:dict

def load_json():
    with open('appdata.json') as jsfile:
        return json.load(jsfile)

def update_json(data: dict):
    with open('appdata.json', 'w') as jsfile:
        json.dump(data, jsfile, indent=2)

# notifier
def _notify(msg, icon=COFFE_ICO, title=None, soundfile=DOLPHIN_WAV):
    toaster.show_toast(
        title=title if title else "Notification",
        msg=msg,
        icon_path=icon,
        threaded=True,
    )

    if soundfile:
        winsound.PlaySound(soundfile, flags=winsound.SND_FILENAME)


def sed_alert():
    dt = load_json()

    if dt["sedentary_alert"]:
        interval_secs = 5 #dt["interval"] * 60
        sleep(interval_secs)

        _notify(
            msg = "Take a break and hydrate. Do some stretching.",
        )

        sed_alert()