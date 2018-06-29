import json
import urllib.request

contacts = urllib.request.urlopen("https://api.androidhive.info/contacts/").read()
jsontopython=json.loads(contacts)
print(str(contacts))
output = jsontopython['contacts']
print(output)
first = output[0]
#print(first)
#print(first["name"])
