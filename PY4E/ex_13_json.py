import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2063198.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

info = json.loads(data)

total_count = 0
total_sum = 0

for item in info['comments']:
    count = item['count']
    total_sum += count
    total_count += 1

print('Count:', total_count)
print('Sum:', total_sum)
