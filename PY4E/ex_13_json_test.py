import urllib.request, urllib.parse
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'http://py4e-data.dr-chuck.net/opengeo?'

address = input('Enter location: ')

params = {'q': address}
url = service_url + urllib.parse.urlencode(params)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'features' not in js or len(js['features']) == 0:
    print('Failed to retrieve plus_code')
else:
    plus_code = js['features'][0]['properties'].get('plus_code', 'No plus_code found')
    print('Plus code:', plus_code)