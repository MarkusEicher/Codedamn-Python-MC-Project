from tkinter import Tk, ttk, StringVar, IntVar
from _app import *

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

def toggle_sed_alert():
    print(sedentary_alert.get())


sed_check = ttk.Checkbutton(
    frame, variable= sedentary_alert,
    text = "Sedentary Alert", command=toggle_sed_alert
)
sed_check.grid(column=0, row=0, pady=10)





App.mainloop()