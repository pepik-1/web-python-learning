lines = [
    "P-1;Mouse;25;Periphery",
    "P-2;Keyboard;45;Periphery",
    "P-3;Cloud VM;120;Services",
    "P-2;Duplicate;50;Periphery",
    "P-4;Broken;-5;Services",
    "P-5;BadPrice;abc;Services",
]


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False
    
    # TODO: вернуть True, если text можно считать числом (включая дроби и знак), иначе False
    


class Product:
    def __init__(self,id, name, price, category):
        self.id = id
        self.name = name
        self._price = price
        self.category = category

    @property
    def price(self):
        return self._price
    
    
    def set_price(self,value: float) -> bool:
        if isinstance(value(int,float)) and value >= 0:
            self._price = float(value)
            return True
        return False
    
    @classmethod
    def from_line(cls,raw):
        parts = raw.split(';')
        if len(parts) != 4:
            return None, "Wrong number of columns"
        
        id, name, price_str, category = parts
        
        if not is_number(price_str):
            return None, f"Invalid price: {price_str}"
        
        price = float(price_str)
        if price < 0:
            return None, f"Negative price: {price}"
            
        return cls(id, name, price, category), None




    # TODO: __init__(id, name, price, category)
    # TODO: property price (только getter)
    # TODO: set_price(value) -> bool
    # TODO: classmethod from_line(cls, raw) -> (product_or_none, reason)
    


class ProductRegistry:
    def __init__(self): 
        self.products = []
        self.ids = set()

    def add(self, product) -> (bool, str):
        if product.id in self.ids:
            return False, "ID already exists"
        self.products.append(product)
        self.ids.add(product.id)
        return True, "Success"
        
    def count(self):
        return len(self.products)
    
    def all_products(self):
        return self.products
    
    def has_id(self, id):
        return id in self.ids
    
    def by_category(self, category):
    
        return [p for p in self.products if p.category == category]
    
    def aug_price(self): 
        if not self.products:
            return 0
        total = sum(p.price for p in self.products)
        return total / len(self.products)
    

    # TODO: add(product) -> (bool, reason)
    # TODO: count()
    # TODO: all_products()
    # TODO: has_id(id)
    # TODO: by_category()
    # TODO: avg_price()
    

registry = ProductRegistry()
problems = []


for line in lines:
    product, reason = Product.from_line(line)
    
    if product is None:
        problems.append((line,reason))
        continue

    success, add_reason = registry.add(product)
    if not success:
        
        problems.append((line, add_reason))


# TODO: создать registry и problems
# TODO: пройти по lines, загрузить валидные товары
# TODO: проблемные строки добавлять в problems как (line, reason)
# TODO: вывести count, by_category, avg_price и problems


print(registry.count())
print(len(registry.by_category('Periphery')))
print(registry.aug_price())
print(problems)