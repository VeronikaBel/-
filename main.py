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

def get_shop_list_by_dishes(dishes, person_count):
        cook_book = read_recipes(recipes.txt)
        shop_list = {}
        for dish in dishes:
                for ingredient in cook_book[dish]:
                        ingredient_name = ingredient['ingredient_name']
                        if ingredient_name not in shop_list:
                                shop_list[ingredient_name] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
                        else:
                                shop_list[ingredient_name]['quantity'] += int(ingredient['quantity']) * person_count
        return shop_list