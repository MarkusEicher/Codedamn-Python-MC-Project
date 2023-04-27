from tkinter import Tk, ttk, StringVar, IntVar
from _app import *
from threading import Thread

JSDTA = load_json()

App = Tk()
App.title("Sedentary Alert")
App.iconbitmap(APP_ICO)
App.resizable(True, True)

App.tk.call("source", SUN_VALLEY_THEME)
App.tk.call("set_theme", "dark")

# User interface

frame = ttk.Frame(App, padding=10)
frame.grid(column=0, row=0, padx=10, pady=10)


sedentary_alert = IntVar()
sedentary_alert.set(
    1 if JSDTA["sedentary_alert"] else 0
)

def toggle_sed_alert():
    JSDTA["sedentary_alert"] = bool(sedentary_alert.get())
    update_json(JSDTA)

    if JSDTA["sedentary_alert"] and\
        not SED_TREAD.is_alive():
        init_sed_thread()
        SED_TREAD.start()


sed_check = ttk.Checkbutton(
    frame, variable=sedentary_alert,
    text = "Sedentary Alert", command=toggle_sed_alert
)
sed_check.grid(row=0, column=0, columnspan=2, pady=5)

sed_lbl = ttk.Label(frame, text="Interval")
sed_lbl.grid(row=1, column=0, pady=5)

interval_options = ["15 Min", "20 Min", "30 Min", "45 Min", "60 Min"]
interval_period = StringVar()
# interval_period.set(f"{JSDTA['interval']} Min")

def interval_change (interval: str):
    JSDTA["interval"] = int(interval.split(" ")[0])
    update_json(JSDTA)

interval_dropdown = ttk.OptionMenu(
    frame, interval_period, "Select", *interval_options, command=interval_change
)
interval_dropdown.grid(row=1, column=1, padx=(10, 0))

interval_period.set(f"{JSDTA['interval']} Min")

# Create a Thread

def init_sed_thread():
    global SED_TREAD
    SED_TREAD = Thread(
        target=sed_alert,
        daemon=True
    )

init_sed_thread()

if JSDTA["sedentary_alert"]:
    SED_TREAD.start()

App.mainloop()