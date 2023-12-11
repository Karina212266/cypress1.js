import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/reg',
              json={
                  "trainer_token": "871ef3a65475cbc5c144a2814870239d",
                   "email": "suvorovakd@yandex.ru",
                   "password": "Karish_Parish1"
                   },
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/confirm_email',
              json={"trainer_token": "871ef3a65475cbc5c144a2814870239d"},
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
              json={
                   "name": "круассан",
                   "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
              headers={'Content-Type': 'application/json', 'trainer_token': '871ef3a65475cbc5c144a2814870239d'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
             json={
                 "pokemon_id": "21466",
                 "name": "kruassan",
                 "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                 headers={'Content-Type': 'application/json', 'trainer_token': '871ef3a65475cbc5c144a2814870239d'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

requests.put(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
             json={"pokemon_id": "21466"},
             headers={'Content-Type': 'application/json', 'trainer_token': '871ef3a65475cbc5c144a2814870239d'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.get(url='https://api.pokemonbattle.me:9104/trainers',
              json={
                  "trainer_token": "871ef3a65475cbc5c144a2814870239d"
                   },
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

if response.status_code == 200:
    print('Ok!')
else:
    print('Bad!')
    
