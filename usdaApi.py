from urllib import request
import requests
from pprint import pprint
import os

#need to seperate key using os.environ
url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

# todo keys in environment variables 
# share keys with each other in slack or email 
# everyone sets three environment variables with the same name and value
api_key='XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8'
#key = os.envrion.get('USDA_KEY')


def get_food_nutrition(ingredient):
    try:
        
        query = build_query(ingredient, api_key)
        response = make_api_request(url, query)
        
        nutrition_data = get_nutrition(api_data)

        return nutrition_data, None

    except Exception as ex:
        print(ex)
        print(response.text) #for debugging print, might want to log for developing 
        return None, ex


def make_api_request(url, query):
    response = requests.get(url, params=query)
    response.raise_for_status()#raise exception for 400 or 500 errors
    api_data = response.json()#may error if response is not json
    return api_data


def build_query(ingredient, api_key):
    # TODO error handling - what if ingredient or API key are missing? 
    if not ingredient:
        raise ValueError('No ingredient')

    query = {
        'query': ingredient, 
        'api_key': api_key, 
        'pageSize': 2 } #query string

    # todo is there a way to request smaller number of results? 
    return query
        


def get_nutrition(food_data):
     try:

         # todo get first result
         # extract 2-3 pieces of information
         # return as an object 
        
        nutrition = food_data['foods']
        # return nutrition

        # just for example - you would choose what 
        # data to return and how to structure it
        return { 
            'calories': 500,
            'sugar': 3
        }

     except KeyError:
         print('This data is not in the format expected')
         return 'Unknown'


if __name__ == '__main__':
    main()
