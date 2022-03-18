from flask import Flask, render_template, request
from recipes_api import get_API_edamam
# from usdaApi import get_ingredient
from usdaApi import get_food_nutrition

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
        nutrition, error = get_food_nutrition(food)
        if error: 
            # something went wrong getting data 
            pass # todo report error in user-friendly way 
            print('error usda api', error)
        elif nutrition:
            # things worked and we have data 
            pass  # todo
        # todo images from flickr
        return render_template('search_result.html', find_query=food , recipe=recipe, nutrition=nutrition)
    else:
        return render_template('error.html')


@app.route('/save', methods=['POST'])
def save_bookmark():
    data = request.form 
    print(data)
    recipe_title = request.form["recipe_title"]   # get one piece of data 
    print(recipe_title)

    # todo make a Bookmark object
    # save it to the database 
    # error handling 
    
    return "todo"  # render the bookmarks page ? 


if __name__ == '__main__':
    app.run()