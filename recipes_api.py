from unittest import result
import requests 
from pprint import pprint

application_id = '82fad7ff'
applications_keys = '66a21d5e09d78723c3f5153046e1386c'

def get_API_edamam(query):
    base_url = 'https://api.edamam.com/api/recipes/v2'
    query = {'app_id': application_id, 'app_key': applications_keys, 'type': 'public', 'q': {query}}
    data = requests.get(base_url, params=query).json()
    response = extract_data(data)
    return response

def extract_data(data):
    recipes = { 'title': [],
            'ingredients': [],
            'calories':[],
            'calories_quantity': [],
            'image': []}
    for x in range(5):                         #limit to 5 recipes
        recipe = data['hits'][x]['recipe']
        title = recipe['label']
        ingredients = recipe['ingredientLines']
        calories = recipe['totalNutrients']['ENERC_KCAL']['unit']
        calories_quantity = recipe['totalNutrients']['ENERC_KCAL']['quantity']
        image = recipe['image']
        recipes['title'].append(title)
        recipes['ingredients'].append(ingredients)
        recipes['calories'].append(calories)
        recipes['calories_quantity'].append(round(calories_quantity, 2))
        recipes['image'].append(image)
    return recipes
