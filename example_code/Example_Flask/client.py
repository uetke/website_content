import requests

addr = 'http://localhost:5000'
r = requests.get(addr + "/idn")

print(r.content)
