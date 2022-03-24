from flask import Flask, render_template, request
from recipes_api import get_API_edamam
from database import add_recipe_bookmark
from usdaApi import get_food_nutrition
from flickr_Api import get_photo_flickr

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search')
def search():
    print(request.args)
    find_query = request.args.get('query')
    print(find_query)

    # how are you handling errors? 

    if find_query:
        recipe = get_API_edamam(find_query)
        flickr = get_photo_flickr(find_query)
        nutrition = get_food_nutrition(find_query)
        print(nutrition)
        return render_template('search.html',find_query=find_query , recipe=recipe, flickr=flickr, nutrition=nutrition[0])
    else:
        return render_template('error.html')

@app.route('/save', methods=['POST'])
def save_bookmark():

    # how are you handling errors, for example, saving duplicate foods? 

    data = request.form 
    print(data)
    food = request.form["food"]
    title = request.form["recipe_title"]
    ingredients = request.form["recipe_ingredients"]
    calories = request.form["recipe_calories"]
    url = request.form["recipe_photo_url"]   
    data_from_database = add_recipe_bookmark(food, title, ingredients, calories, url)
    return render_template('saved_recipes.html', data_from_database=data_from_database) 

if __name__ == '__main__':
    app.run()