from urllib import request
import requests 
from pprint import pprint
import os

application_id = '82fad7ff'
applications_keys = '66a21d5e09d78723c3f5153046e1386c'

user_input = 'tomato'

base_url = 'https://api.edamam.com/api/recipes/v2'

query = {'app_id': application_id, 'app_key': applications_keys, 'type': 'public', 'q': user_input}

data = requests.get(base_url, params=query).json()
if data:
    for x in range(0,5):

        recipe = data['hits'][x]['recipe']
        title = data['hits'][x]['recipe']['label']
        print(title)
        ingredients = data['hits'][x]['recipe']['ingredientLines']
        for a in ingredients:
            print(a)
        nutrients_calories = recipe['totalNutrients']['ENERC_KCAL']['unit']
        nutrients_calories_quantity = recipe['totalNutrients']['ENERC_KCAL']['quantity']
        print(f'{nutrients_calories} = {nutrients_calories_quantity:.2f}')

        print('\n')

else:
    print('no data')