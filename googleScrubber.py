import json, urllib, urllib.request, requests

obj = requests.get("https://play.google.com/store/search?q=voya&c=apps&hl=en").json()

#str_response = urllib.request.urlopen("https://play.google.com/store/search?q=voya&c=apps&hl=en").read().decode('utf-8')
#obj = json.loads(str_response)
#I'm guessing this would output the html source code?
print(obj)