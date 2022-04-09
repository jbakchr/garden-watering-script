from datetime import datetime
import json
import tkinter as tk
from tkinter import ttk

import requests
import pyautogui

city = requests.utils.quote("Hillerød")
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%B")
date_number = datetime.now().day

url = f"https://www.dmi.dk/dmidk_obsWS/rest/archive/daily/danmark/precip/{city}/{year}/{month}"
r = requests.get(url)
data = json.loads(r.text)

rain_amount = 0
if date_number >= 3:
    for i in range(date_number - 1, (date_number - 3), -1):
        rain_amount += data["dataserie"][i]["valueRounded2OneDecimal"]

if rain_amount > 1.0:
    root = tk.Tk()

    ttk.Label(root, text="Perhaps you should water the garden",
              padding=(20, 20)).pack()

    ok_button = ttk.Button(root, text="OK", command=root.destroy)
    ok_button.pack()

    root.mainloop()
    # pyautogui.confirm(text="Perhaps you should water to garden ..",
    #   title="Awesome Garden Watering App", buttons=['OK'])
