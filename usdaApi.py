from urllib import request
import requests
from pprint import pprint
import os

#need to seperate key using os.environ
url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
api_key='XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8'
#key = os.envrion.get('USDA_KEY')

def get_food_nutrition(ingredient):
    try:
        
        query ={'query': ingredient, 'api_key': api_key, 'pageSize':2} #query string
        response = requests.get(url, params=query)
        response.raise_for_status()#raise exception for 400 or 500 errors
        data = response.json()#may error if response is not json
        response = get_nutrition(data)
        return response, None
    except Exception as ex:
        print(ex)
        return None, ex


def get_nutrition(food_data):
     try:
         #extract 2-3 data, return as object
        data = []
        for x in range(len(food_data['foods'][0]['foodNutrients'])):
            nutrition = food_data['foods'][0]['foodNutrients'][x]['nutrientName']
            print(nutrition)
            data.append(nutrition)
        return data
     except KeyError:
         print('This data is not in the format expected')
         return 'Unknown'

