from dataclass import dataclass 

@dataclass
class Bookmark:
    food : str        # -- search query 
    recipe_title: str   #  --from edamanm
    ingredients : str    # --- join the list into a string, convert string to list when reading 
    recipe_calories : str
    recipe_image_url : str
    ingredient_calories : float      #-- from usda
    ingredient_sugar : float 
    ingredient_fat : float 
    ingredient_picture : str  #  -- from flikr