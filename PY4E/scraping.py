from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('span')

total = 0

for tag in tags:
    content = tag.get_text()
    numbers = re.findall(r'[0-9]+', content)
    total += sum(int(num) for num in numbers)

print('Total sum:', total)
