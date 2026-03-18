lines = [
    "P-1;Mouse;25;Periphery",
    "P-2;Keyboard;45;Periphery",
    "P-3;Cloud VM;120;Services",
    "P-2;Duplicate;50;Periphery",
    "P-4;Broken;-5;Services",
    "P-5;BadPrice;abc;Services",
]


def is_number(text):
    if int(text):
        return True
    else:
        return False
    
    # TODO: вернуть True, если text можно считать числом (включая дроби и знак), иначе False
    


class Product:
    def __init__(self,id, name, price, category):
        self.id = id
        self.name = name
        self._price = price
        self.category = category

    def property_price(self):
        return self._price
    
    def set_price(self,value: float) -> bool:
        if isinstance(value(int,float)) and value >= 0:
            self._price = float(value)
            return True
        return False
    
    @classmethod
    def from_line(cls,raw):
        product_or_none = []
        accept_names = {'Mouse','Keyboard','Cloud VM'}
        id,name,price,category = raw.split(';')
        try:
            raw.split(';') == 4
            name in accept_names
        except ValueError as e:
            product_or_none.append(name)

        # я не до конца понял что нужно сделать и какие причины куда добавлять


    # TODO: __init__(id, name, price, category)
    # TODO: property price (только getter)
    # TODO: set_price(value) -> bool
    # TODO: classmethod from_line(cls, raw) -> (product_or_none, reason)
    


class ProductRegistry:
    # TODO: __init__ (products list + id set)
    def __init__(self,products,list,id,set):
        self.products = products
        self.list = list
        self.id = id
        self.set = set

    def add(self,product:str) -> bool:
        if product in self.products:
            return False + "already exists"
        return True + 'yeee'
        
    def count(self):
        count += 1
        return count
    
    def all_products(self):
        all = []
        all.append(self.products)
        return all
    
    def has_id(self,id):
        if id != None:
            return True
        return False
    
    def by_category(self,category):
        categories = {'Periphery','Services'}
        if category not in categories:
            return 0
        count += 1
        good = {category:count}
        return good
    
    def aug_price(self):
        total = sum(p.price for p in self.products)
        return total/len(self.products)
    

    # TODO: add(product) -> (bool, reason)
    # TODO: count()
    # TODO: all_products()
    # TODO: has_id(id)
    # TODO: by_category()
    # TODO: avg_price()
    


# TODO: создать registry и problems
# TODO: пройти по lines, загрузить валидные товары
# TODO: проблемные строки добавлять в problems как (line, reason)
# TODO: вывести count, by_category, avg_price и problems
