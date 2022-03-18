from unittest import result
import requests 
from pprint import pprint

application_id = '82fad7ff'
applications_keys = '66a21d5e09d78723c3f5153046e1386c'

def get_API_edamam(query):
    # todo error handling 
    base_url = 'https://api.edamam.com/api/recipes/v2'
    query = {'app_id': application_id, 'app_key': applications_keys, 'type': 'public', 'q': {query}}
    data = requests.get(base_url, params=query).json()
    response = extract_data(data)
    return response

def extract_data(data_from_api):

    # print(data_from_api)
    if data_from_api:  # if list has any data 
        recipe = data_from_api['hits'][0]['recipe']
        title = recipe['label']
        ingredients = recipe['ingredientLines']
        calories = recipe['totalNutrients']['ENERC_KCAL']['unit']
        calories_quantity = recipe['totalNutrients']['ENERC_KCAL']['quantity']
        image = recipe['image']

        return {
            'title': title,
            'ingredients': ingredients,
            'calories': calories,
            'calories_quantity': calories_quantity,
            'image': image  
        }

    else:
        None   # todo decide what to return here
        