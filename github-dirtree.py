import requests
import json
import sys

input_regex = sys.argv[1].replace("https://github.com/", "")

website = "https://api.github.com/repos/" + input_regex + "/git/trees/master?recursive=1"
response = requests.get(website)
a = response.json()
for b in a['tree']:
	print(b['path'])
