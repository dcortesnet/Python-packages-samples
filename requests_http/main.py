import requests

url = "https://pokeapi.co/api/v2/"
response = requests.get(url)

print(response)
print(response.json())