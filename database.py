# bookmarks database 

# create database here 


create_table_sql = """ 
CREATE TABLE bookmarks (
    food TEXT,           -- search query 
    recipe_title, TEXT,     --from edamanm
    ingredients TEXT,      --- join the list into a string, convert string to list when reading 
    recipe_calories TEXT, 
    recipe_image_url TEXT,
    ingredient_calories FLOAT,     -- from usda
    ingredient_sugar FLOAT,
    ingredient_fat FLOAT,
    ingredient_picture TEXT    -- from flikr
)

"""

def add_recipe_bookmark(bookmark):
    pass 
    # reading list app does something similar with Book object 
    # store in the database 


def get_all_bookmarks():
    pass 
    # query database, return list of Bookmark objects 