import urllib.request
f = urllib.request.urlopen("https://ifconfig.co/")
print(f.read())
