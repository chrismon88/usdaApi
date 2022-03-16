from flask import Flask, render_template, request
from recipes_api import get_API_edamam

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search')
def search():
    print(request.args)
    find_query = request.args.get('query')
    if find_query:
        recipe = get_API_edamam(find_query)
        return render_template('search.html',find_query=find_query , recipe=recipe)
    else:
        return "error"

if __name__ == '__main__':
    app.run()