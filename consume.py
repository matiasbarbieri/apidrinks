import requests

response = requests.get('http://localhost:8000/drinks/')
#response = requests.get('https://catfact.ninja/fact')
print(response.json()) # print the JSON response