
import requests


r = requests.get('https://api.github.com/events')
print(r.text)
print(r.status_code)