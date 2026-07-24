import requests


r = requests.get("https://wttr.in/")
print(r.text)
