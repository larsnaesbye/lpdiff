import sys
import requests
import jsondiff as jd
import json
from jsondiff import diff

urls = sys.argv[1:len(sys.argv)]
jsons = []
for url in urls:
    response = requests.get(url)
    jsons.append(response.json())
for j in range(len(jsons)):
    for k in range(len(jsons)):
        result = jd.diff(jsons[j], jsons[k])
        if j < k:
            print(json.dumps(result, indent=0))
