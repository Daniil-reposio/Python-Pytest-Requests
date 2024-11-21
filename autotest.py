import requests

URL = "https://api.pokemonbattle.ru"
TOKEN = "57155810080165ed507c4228e869e124"
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

Body_create = {
    "name": "Покемонч",
    "photo_id": 17
} 

Body_change = {
    "pokemon_id": "143557",
    "name": "Лучший",
    "photo_id": 5
}

Body_get = {
    "pokemon_id": "143557"
} 

task_responce_one = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = Body_create)

bring_code_one = task_responce_one.json()['id'], task_responce_one.json()['message']

print ('Cтатус код =',f'{task_responce_one.status_code},', 'текст ответа -',task_responce_one.text)

print (f'Вывод id и message - {bring_code_one}')




task_responce_two = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = Body_change) 

bring_code_two = task_responce_two.json()['message'] 

print ('Cтатус код =',f'{task_responce_two.status_code},', 'текст ответа -',task_responce_two.text) 

print (f'message - {bring_code_two}')




task_responce_three = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = Body_get) 

bring_code_three = task_responce_three.json()['message'] 

print ('Cтатус код =',f'{task_responce_three.status_code},', 'текст ответа -',task_responce_three.text)

print (f'message - {bring_code_three}')




# f'{URL}/v2/pokemons' f'{переменная}строка' - f{} позволяет совмещать переменные и строки
# (import requests(название библиотеки))
# (python -m pip install requests) - запипать библиотеку  
# (pip3 install pytest) - тоже запипать библиотеку 
# (pip3 --version) - проверить версию pip3 