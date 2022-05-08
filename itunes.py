import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit

response = requests.get(
    "https://itunes.apple.com/search/?entity=song&limit=1&term="+sys.argv[1])

results = response.json()
# print(json.dumps(response.json(), indent=2))
# print(results["results"])
for result in results["results"]:
    print(result["trackName"])
