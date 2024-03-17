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
for j in range(len(jsons)):
    for k in range(len(jsons)):
        result = jd.diff(jsons[j], jsons[k])
        if j < k:
            print(result)
