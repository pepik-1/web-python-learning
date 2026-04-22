# Model
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

class CardModel:
    def __init__(self):
        self.products = {
            'apple':Product('apple',80),
            'banana':Product('Banana',60),
            'coffe': Product('coffe',250)
        }
        self.items = []

    def add_item(self,product_code:str):
        if product_code not in self.products:
            raise ValueError('No found in catalog')
        self.items.append(self.products[product_code])

    def total(self):
        return sum(item.price for item in self.items)
    
    def item_names(self):
        return [item.name for item in self.items]
    
model = CardModel()
model.add_item('apple')
model.add_item('banana')
print(model.item_names())
print(model.total())

# view
class ConsoleCartView:
    @staticmethod
    def render_cart(items,total):
        print('Trash:')

        if items:
            for item in items:
                print(f'- {item}')
        else:
            print(f'- empty')
        print(f'overall: {total}')
    
    @staticmethod
    def render_error(msg):
        print(f'Error: {msg}')
    
ConsoleCartView.render_cart(['Apple','Coffe'],330)

class CartController:
    def __init__(self,model:CardModel,view: ConsoleCartView):
        self.model = model
        self.view = view

    def add_product(self,product_code):
        try:
            self.model.add_item(product_code)
            self.view.render_cart(self.model.item_names(),self.model.total())
        except ValueError as e:
            self.view.render_error(str(e))

controller = CartController(CardModel(),ConsoleCartView())
controller.add_product('banana')
controller.add_product('coffe')
controller.add_product('water')

