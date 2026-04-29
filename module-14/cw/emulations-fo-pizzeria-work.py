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
            0: Recipe('pizza-1',['dough','cheese','tomatoes','mayonnaise','chicken']),
            1: Recipe('pizza-2',['dough','cheese','tomatoes','ketchup','chicken']),
            2: Recipe('pizza-3',['dough','cheese','tomatoes','chicken'])
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
        'chicken': Ingredient('chicken','chicken',666,228),
        'ketchup': Ingredient('ketchup','ketchup',15,3),
    }

def create_stock():
    return {
        'dough':10,
        'cheese':10,
        'tomatoes': 10,
        'mayonnaise':10,
        'chicken': 10,
        'ketchup': 10
    }
def get_topping():
    return{ 
        'tomatoes',
        'mayonnaise',
        'chicken',
        'ketchup'
    }

def create_custom_recipe(inventory:Inventory) -> Recipe:
    builder = PizzaBuilder()
    print('own pizza creation')

    for key in get_topping():
        ingredient = inventory.ingredients[key]

        choise = input(f'do you want to add {ingredient.name}') 

        if choise == 'Yes':
            builder.add_ingredient(ingredient.key)

        return builder.build()

class Inventory:
    def __init__(self,ingredient: list[str, Ingredient],stock):
        self.ingredients = ingredient
        self.stock = stock

    def has_enough(self,ingredienct_keys: list[str, Ingredient] ,quantity) -> bool:
        for key in ingredienct_keys:
            if self.stock.get(key,0) < quantity:
                return False
            return True

    def reduce_stock(self,ingredienct_keys: list[str, Ingredient] ,quantity):
        for key in ingredienct_keys:
            self.stock[key] -= quantity

    def show(self):
        print('ingredients available')
        for key,count in self.stock.items():
            ingredient = self.ingredients[key]
            print(f'{ingredient.name}:{count}')
            

class SalesReport:
    def __init__(self):
        self.profit = 0
        self.revenue = 0
        self.sold_count = 0
    
    def add_order(self,order:Order,ingredients: list[str, Ingredient]):

        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print('summary')
        print(f'pizzas sold: {self.sold_count}')
        print(f'profit: {self.profit}')
        print(f'revenue:{self.revenue}')

def show_menu():
    print('1.create order')
    print('2. summary')
    print('3. ingredients available')
    print('4.Exit')

def show_standart_recipes(recipes:dict[str,Recipe],ingredients:dict[str,Ingredient]):
    print('default pizzas')
    for number, recipe in recipes.items():
        print(f'{number}. {recipe.name}')
    price=sum(ingredients[key].price for key in recipe.ingredient_keys)
    print(f'one item price: {price}')

def choose_recipe(recipes:dict[str,Recipe],ingredients:dict[str,Ingredient],inventory:Inventory):



    while True:
        choise = input('choose a point:')

        if choise == 0:
            pass
        else:
            return recipes[int(choise)]
        
    
        
def choose_payment():
    print('choose payment way:')
    print('1 - cash')
    print('2 - card')
    
    while True:
        choice = input('choose:')
        if choice == '1':
            return CashPayment()
        elif choice == '2':
            return CardPayment()
        

        


def create_order(
        ingredients: dict[str,Ingredient],
    inventory: Inventory,
    report: SalesReport,
    file_saver:FileOrderSaver
):
    recipes = RecipeFactory.get_standard_recipes()
    items: list[OrderItem] = []
    while True:
        show_standart_recipes(recipes,ingredients)

        recipe = choose_recipe(recipes,ingredients,inventory)
        quantity = int(input('enter quantity:'))

        if not inventory.has_enough(recipe.ingredient_keys,quantity):
            print('run out of ingredients for an order')
            return 
        
        items.append(OrderItem(recipe,quantity))

        more = input('will you add one more pizza?')

        if more == 'No':
            break

    payment_strategy, payment_type = choose_payment()

    order = Order(items,payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys,item.quantity)

    amount = order.total_price(ingredients)
    print(payment_strategy.pay(amount))

    file_saver.save(order,ingredients)

    report.add_order(order,ingredients)
    



def main():
    
    ingredients = create_ingredients()
    stock = create_stock()

    inventory = Inventory(ingredients,stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()

        choice = input('select a point in a menu: ')

        if choice == '1':
            create_order(ingredients,inventory,report,file_saver)
        elif choice == '2':
            report.show()
        elif choice == '3':
            inventory.show()
        elif choice == '4':
            break

main()

