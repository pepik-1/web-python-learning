from dataclasses import dataclass

@dataclass
class Ingredient:
    name:str
    key:str
    price:str
    cost:str

@dataclass 
class Recipe:
    name:str
    ingredients_keys:list[str]

class RecipeFactory:
    def default_recepies(self):
        return {
            0:('hot-dog 1',Recipe['dough','sausage','ketchup','mayonnaise','onion']),
            1:('hot-dog 2',Recipe['dough','sausage','ketchup','cucumber','onion']),
            2:('hot-dog 3',Recipe['dough','sausage','ketchup','salad'])
        }