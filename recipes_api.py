from unittest import result
import requests 
import random
from pprint import pprint

# remove keys from GitHub
application_id = '82fad7ff'
applications_keys = '66a21d5e09d78723c3f5153046e1386c'
base_url = 'https://api.edamam.com/api/recipes/v2'
random_number = random.randint(0,9)  # this is set once when this module is loaded.

def get_API_edamam(user_input):
    try: 
        query = build_query(user_input, application_id, applications_keys)
        response = make_api_request(base_url, query)
        recipe = extract_data(response)
        return recipe  # return a tuple of recipe, None, the same structure as the error response
    except Exception as exc:
        print(exc)
        return None, exc
    
def make_api_request(url, query):
    response = requests.get(url, params=query)
    response.raise_for_status()                            #raise exception for 400 or 500 errors
    api_data = response.json()                              #may error if response is not json
    return api_data

def build_query(user_input, id, keys):
    if not user_input:
        raise ValueError('No ingredient') 
    query = {
    'app_id': id, 
    'app_key': keys, 
    'type': 'public', 
    'q': user_input}    # this probably doesn't need to be a set
    return query

def extract_data(data_from_api):
    # what will this do if the JSON is not in the format you expect? 
    # need to anticipate errors reading the response data

    # if you want a new random number every time, need to set this here
    # base it on the number of recipies returned 
    recipe_count = len(data_from_api['hits'])
    random_number = random.randint(0, recipe_count) 


    if data_from_api:                            # if list has any data 
        recipe = data_from_api['hits'][random_number]['recipe']         #return a different recipe for the user, even if the user input is the same
        title = recipe['label']
        ingredients = recipe['ingredientLines']
        calories_quantity = recipe['totalNutrients']['ENERC_KCAL']['quantity']
        image = recipe['image']
        return {
            'title': title,
            'ingredients': ingredients,
            'calories_quantity': round(calories_quantity, 2),
            'image': image  
        }
    else:
        return 'No data was found from API'
        