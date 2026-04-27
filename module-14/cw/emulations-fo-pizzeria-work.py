from dataclasses import dataclass
from abc import ABC,abstractmethod
@dataclass
class Ingredient:
    name:str
    key: str
    price:float
    cost:float

@dataclass
class Recipe:
    name:str
    ingredient_keys: list[str]

class RecipeFactory:
    def get_standard_recipes() -> dict[int,Recipe]:
        return {
            0: Recipe('pizza-1',['dough','cheese','tomatoes','mayonnaise','chiken']),
            1: Recipe('pizza-2',['dough','cheese','tomatoes','ketchup','chiken']),
            2: Recipe('pizza-3',['dough','cheese','tomatoes','chiken'])
        }

class PizzaBuilder:
    def __init__(self):
        self._ingredient = ['dough','cheese']
    
    def add_ingredient(self,key:str):
        if key not in self._ingredient:
            self._ingredient.append(key)
        return self
    
    def build(self):
        return Recipe('own pizza', self._ingredient)
    
@dataclass 
class Order:
    payment_type:str

    def to_text(self,ingredient:dict[str,Ingredient]) -> str:
        lines = ['order info:']

@dataclass
class OrderItem:
    recipe:Recipe
    quantity:int

    def total_cost(self,ingredients:dict[int,Ingredient]) -> float:
        one_pizza_cost = sum(ingredients[key].price for key in self.recipe.ingredient_keys)
        return one_pizza_cost * self.quantity
    
@dataclass 
class Order:
    items:list[OrderItem]
    payment_type: str

    def total_price(self,ingredients:dict[str,Ingredient]) -> str:
        return sum(item.total_price(ingredients) for item in self.items)
    
    def total_cost(self,ingredients:dict[str,Ingredient]) -> str:
        return sum(item.total_cost(ingredients) for item in self.items)
    
    def total_profit(self,ingredients:dict[str,Ingredient]):
        return self.total_price(ingredients) - self.total_cost(ingredients)
    


    def to_text(self,ingredients:dict[str,Ingredient]) -> str:
        lines = ['order info']

        for item in self.items:
            ingredients_names = [
                ingredients[key].name for key in item.recipe.ingredient_keys
            ]

            lines.append(f'pizza: {item.recipe.name}')
            lines.append(f'quantity: {item.quantity}')
            lines.append(f'contain:')

            for name in ingredients_names:
                lines.append(f'- {name}')

            lines.append(f'position price: {item.total_price(ingredients)} rub')

        lines.append(f'payment type:{self.payment_type}')
        return '\n'.join(lines)

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,ammount:float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self,amount:float):
        return f'pay with cash for the {amount} rub'
    
class FileOrderSaver:
    def __init__(self,filename: str = 'order.txt'):
        self.filename = filename
    def save(self,order:Order,ingredients:dict[str,Ingredient]):
        with open(self.filename,'a',encoding='utf-8') as file:
            file.write(order.to_text(ingredients))
            file.write('\n' + '-' * 50 + '\n')

def create_ingredients():
    return {
        'dough': Ingredient('dough','dough',70,30),
        'cheese': Ingredient('cheese','cheese',80,20),
        'tomatoes': Ingredient('tomatoes','tomatoes',20,5),
        'mayonnaise': Ingredient('mayonnaise','mayonnaise',50,10),
        'chiken': Ingredient('chiken','chiken',666,228),
        'ketchup': Ingredient('ketchup','ketchup',15,3),
    }
