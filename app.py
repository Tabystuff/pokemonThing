import requests
import re

pokeapi = "https://pokeapi.co/api/v2/"

pokemon = input("What pokemon do you wanna look up? ")
pokemonUrl = f"pokemon/{pokemon}"
pokedexUrl = f"pokemon-species/{pokemon}"

res = requests.get(f"{pokeapi}{pokemonUrl}")
resPokedex = requests.get(f"{pokeapi}{pokedexUrl}")


print(res.url)
print(resPokedex.url)
pokedexEntry = re.sub("[\n\u000c]"," ", resPokedex.json()["flavor_text_entries"][3]["flavor_text"] )


print(pokedexEntry)