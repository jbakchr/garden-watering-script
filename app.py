from datetime import datetime
import requests
import json

city = requests.utils.quote("Hillerød")
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%B")
date_number = datetime.now().day


url = f"https://www.dmi.dk/dmidk_obsWS/rest/archive/daily/danmark/precip/{city}/{year}/{month}"
r = requests.get(url)
data = json.loads(r.text)

# print(data["dataserie"][2])

rain_amount = 0
if date_number >= 2:
    for i in range(date_number - 1, (date_number - 3), -1):
        rain_amount += data["dataserie"][i]["valueRounded2OneDecimal"]

print(rain_amount)
