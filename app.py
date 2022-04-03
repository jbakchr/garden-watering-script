from datetime import datetime
import requests
import json

city = requests.utils.quote("Hillerød")
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%B")

url = f"https://www.dmi.dk/dmidk_obsWS/rest/archive/daily/danmark/precip/{city}/{year}/{month}"
r = requests.get(url)

data = json.loads(r.text)
