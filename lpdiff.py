import sys
import requests
import jsondiff as jd
from jsondiff import diff

# --- MAIN PROGRAM  ---------------------------------

urls = sys.argv[1:len(sys.argv)]
jsons = []
for url in urls:
    response = requests.get(url)
    # print(response.json())
    jsons.append(response.json())
for idj, j in enumerate(jsons, start=1):
    result = jd.diff(jsons[idj], jsons[idj])
    print(result)
    # print(idj, j)
