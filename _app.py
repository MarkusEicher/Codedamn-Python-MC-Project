import json
from os import path


# assets
SUN_VALLEY_THEME = path.join("sunvalley", "sv.tcl")
APP_ICO = path.join("assets", "app.ico") 
COFFE_ICO = path.join("assets", "coffee.ico")
DOLPHIN_WAV = path.join("assets", "dolphin.wav")

JSDTA:dict

def load_json():
    with open('appdata.json') as jsfile:
        return json.load(jsfile)
