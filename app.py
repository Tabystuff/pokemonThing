import requests
import re
import random

# These are the english entries to the pokedex in the api. I use random.choice to pick one
englishEntries = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,20,21,28,36,44,52,61,71,81,91,101,111,121,131,134]
randomEntry = random.choice(englishEntries)


pokeapi = "https://pokeapi.co/api/v2/"

pokemon = input("What pokemon do you wanna look up? ")
pokemonUrl = f"pokemon/{pokemon}"
pokedexUrl = f"pokemon-species/{pokemon}"

resPokemon = requests.get(f"{pokeapi}{pokemonUrl}")
resPokedex = requests.get(f"{pokeapi}{pokedexUrl}")


print(resPokemon.url)
print(resPokedex.url)
pokemonImg = resPokemon.json()["sprites"]["front_default"]
pokedexEntry = re.sub("[\n\u000c]"," ", resPokedex.json()["flavor_text_entries"][randomEntry]["flavor_text"] )

print(pokedexEntry)
print(pokemonImg)