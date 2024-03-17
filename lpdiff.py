# Compare JSON output from URLS (intended for Logpoint configs)
# Lars Næsbye Christensen, NGC 2024
# Syntax: python lpdiff.py <bearer_token> [url1, url2...]


import sys
import requests
import pprint
import jsondiff as jd
import json
from jsondiff import diff

bearer = sys.argv[1]
headers = {"Authorization": "Bearer " + bearer}
urls = sys.argv[2:len(sys.argv)]
jsons = []
for url in urls:
    response = requests.get(url, headers=headers)
    jsons.append(response.json())
for j in range(len(jsons)):
    for k in range(len(jsons)):
        result = jd.diff(jsons[j], jsons[k], syntax='explicit')
        if j < k:
            pprint.pprint(result)
