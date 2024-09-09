import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

for i in range(count):
    print('Retrieving:', url)
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position].get('href', None)

print('Last URL:', url)
