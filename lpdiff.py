import sys

import requests
from datetime import datetime

# --- MAIN PROGRAM  ---------------------------------
print(
    datetime.fromtimestamp(datetime.now().timestamp()), " Starting lpdiff "
)
uri = sys.argv[1]
response = requests.get(uri)
print(response.json())

print(
    datetime.fromtimestamp(datetime.now().timestamp()), " Ending lpdiff "
)
