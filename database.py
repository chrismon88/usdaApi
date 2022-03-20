import sqlite3

db = 'bookmarks.sqlite'
create_table_sql = 'CREATE TABLE IF NOT EXISTS bookmarks (food TEXT, recipe_title TEXT, ingredients TEXT, recipe_calories FLOAT, recipe_image_url TEXT, UNIQUE(recipe_title))'

def add_recipe_bookmark(food, title, ingredients, calories, url):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute(create_table_sql)
            conn.execute('INSERT or IGNORE INTO bookmarks VALUES (?, ?, ?, ?, ?)', (food, title, ingredients, calories, url))
        conn.close()
        data = get_all_bookmarks()
        return data
    except sqlite3.IntegrityError as e:
        raise ValueError('error') from e
        
def get_all_bookmarks():
    with sqlite3.connect(db) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute('SELECT * FROM bookmarks' )
        data_list = []
        for r in rows:
            data_list.append(r)
        return data_list
    conn.close()

