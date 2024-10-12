import requests
#import requsts
from .read_json import read_json
#import information 
import json
#import librory json
data_api = read_json(name_file= 'config_api.json')
#read api from info 
API_KEY = data_api['api_key']
# init constant-api 
CITY_NAME = data_api['city_name']
# init  constant of my city 
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# get url from info uper 
response = requests.get(URL)
#recponse constant of url
if response.status_code == 200:
    # get cicle if
    data_dict = json.loads(response.content)
    #
    print(json.dumps(data_dict, indent= 4))