import requests 
import pytest 



URL = "https://api.pokemonbattle.ru" 
TOKEN = "57155810080165ed507c4228e869e124"
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN} 
Trainer_id = '11405'


def test_codeone():
    trainer_code = requests.get(url = f'{URL}/v2/trainers', headers = HEADER, params = {'trainer_id' : Trainer_id})
    assert trainer_code.status_code == 200

def test_codetwo():
    trainer_code_two = requests.get(url = f'{URL}/v2/trainers', headers = HEADER, params = {'trainer_id' : Trainer_id})
    assert trainer_code_two.json()['data'][0]['id'] == '11405'  