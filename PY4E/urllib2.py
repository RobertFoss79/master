import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in file_handle:
    print(line.decode().strip())
