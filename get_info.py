import requests

url = "https://google.com"

r = requests.get(url)

print(r)
# print(r.text)
# print(r.content)
print(r.json())
