import requests
from datetime import datetime

# --- MAIN PROGRAM  ---------------------------------
print(
    datetime.fromtimestamp(datetime.now().timestamp()), " Starting lpdiff " + version
)

response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
print(response.json())

print(
    datetime.fromtimestamp(datetime.now().timestamp()), " Ending lpdiff " + version
)
