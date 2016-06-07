import json, requests, sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

url = 'https://itunes.apple.com/search?term=voya&entity=software'
response = requests.get(url)
response.raise_for_status()
searchData = json.loads(response.text)
print(searchData)


a = searchData['results']
voyas = []

for i in range(len(a)):
	firstLine = str.splitlines(a[i]['trackName'])[0]
	if ('Voya ' in firstLine) | ('voya ' in firstLine):
		voyas.append(firstLine)

for v in voyas:
	print(v)