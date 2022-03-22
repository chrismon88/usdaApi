from unittest import result
from flask import Flask, render_template, request
from recipes_api import get_API_edamam
from usdaApi import get_food_nutrition
#from database import db need to create db

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search')
def search():
    print(request.args)
    food = request.args.get('query')
    if food:
        recipe = get_API_edamam(food)
        nutrition = get_food_nutrition(food)
#flicker images
        return render_template('search_result.html',find_query=food , recipe=recipe, nutrition=nutrition)
    else:
        return render_template('error.html')


# @app.route('/save-data')
# def save_data():
#     #need to code database/db.py file
#     result = db.save_data('example')
#     print(result)
#     return redirect('/')


if __name__ == '__main__':
    app.run()