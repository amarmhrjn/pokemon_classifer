import requests
import my_data_processor
import my_pokemon_algo

# train the multi-class classifier
my_data_processor.train()

# Get the data from PokeAPI
resp = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()

# (Optionally) process the results
pokemon_data = my_data_processor.process(resp)

# Predict the type of a Pokemon
poke_type = my_pokemon_algo.predict(pokemon_data)

# Example output -> "electric"
print(poke_type)