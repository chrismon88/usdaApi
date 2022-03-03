from urllib import request
import requests
from pprint import pprint

#need to seperate key using os.environ
url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8'

def main():
    ingredients = get_ingredient()
    food_data, error = get_food_ingredient(ingredients) #will save return value in tuple of eather_data and error
    if error:
        print('Sorry, could not locate info on that ingredient')
    else:
        ingredient_nutrition = get_nutrition(food_data)
        print(f'The nutitional value of the ingredient you entered is {ingredient_nutrition}')


def get_ingredient():
    ingredient  = '' # checking input is not empty string
    while len(ingredient)==0:
        ingredient = input('Enter the ingredient you wish to know more about: ').strip()

    ingredients = '{ingrediants}'
    return ingredients


def get_food_ingredient(ingredients):
    try:
        
        #query ={'q': ingredients, 'appid': key} #query string
        response = requests.get(url)
        response.raise_for_status()#raise exception for 400 or 500 errors
        data = response.json()#may error if response is not json
        pprint(data)

        
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text) #for debugging print, might want to log for developing 
        return None, ex

# def get_nutrition(food_data):
#     try:
#         nutrition = food_data[''] ['']
#         return nutrition
#     except KeyError:
#         print('This data is not in the format expected')
#         return 'Unknown'


if __name__ == '__main__':
    main()
