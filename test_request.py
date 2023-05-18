import requests
import time


start = time.time()

for i in range(1, 11):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon["name"])


print(time.time() - start)