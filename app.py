import requests
from flask import Flask, render_template, request
import re
import random

app = Flask(__name__)

@app.route("/", methods=["GET","POST"] )
def index():
    pokeapi = "https://pokeapi.co/api/v2/"

    pokemon = request.form.get("pokemon","haunter")
    pokemonUrl = f"pokemon/{pokemon}"
    pokedexUrl = f"pokemon-species/{pokemon}"

    resPokemon = requests.get(f"{pokeapi}{pokemonUrl}")
    resPokedex = requests.get(f"{pokeapi}{pokedexUrl}")

    # This randomly selects a
    randomEntry = random.choice(range(0,135))

    while resPokedex.json()["flavor_text_entries"][int(randomEntry)]["language"]["name"] != "en":
        print(f"{randomEntry} from while top") 
        print(resPokedex.json()["flavor_text_entries"][int(randomEntry)]["language"]["name"])
        randomEntry = random.choice(range(0,135))
        print(f"{randomEntry} from while bottom")

    print(f"{randomEntry} from outside while")
    pokemonImg = resPokemon.json()["sprites"]["front_default"]
    pokedexEntry = re.sub("[\n\u000c]"," ", resPokedex.json()["flavor_text_entries"][randomEntry]["flavor_text"] )
    return render_template("index.html", pokemon=pokemon, pokemonImg=pokemonImg, pokedexEntry=pokedexEntry )