def read_recipes(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as f:
        while True:
            dish_name = f.readline ().strip ()
            if not dish_name:
                break
            quantity = int (f.readline ().strip ())
            ingredients = []
            for i in range (quantity):
                ingredient = f.readline ().strip ().split (' | ')
                ingredients.append ({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            cook_book = {dish_name: ingredients}
    return cook_book

read_recipes(recipes.txt)