# singleton

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.mode = 'prod'
        return cls._instance
    
# FactoryMethod

class EmailSender:
    def send(self,message):
        return f'Email: {message}'

class SmsSender:
    def send(self,message):
        return f'Sms: {message}'

class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == 'Email':
            return EmailSender()
        if channel == 'Sms':
            return SmsSender()
        raise ValueError('Unknown channel')

sender = NotificationFactory.create('Sms')
print(sender.send('your verification code: 228337'))

# abstract Factory

class LightButton:
    def render(self):
        return 'LightButton'

class LightInput:
    def render(self):
        return 'LightInput'

class DarkButton:
    def render(self):
        return 'DarkButton'
    
class LightThemeFactory:
    def create_button(self):
        return LightButton()
    
    def create_input(self):
        return LightInput()

class  DarkThemeFactory:
    def create_button(self):
        return DarkButton()
    def create_input(self):
        return LightInput()

def built_form(factory):
    button = factory.create_input()
    field = factory.create_input()
    print(button.render(),field.render())

built_form(LightThemeFactory())


# builder

class LaptopBuilder:
    def __init__(self):
        self.laptop = {
            'cpu':'ryzen 5 5600',
            'ram':'16',
            'ssd':'1TB',
            'gpu': 'RX6900XT'
        }

    def for_study(self):
        self.laptop['ram'] = 32
        self.laptop['ssd'] = '2tb'
        return self
    
    def for_gaming(self):
        self.laptop['ram'] = 64
        self.laptop['ssd'] = '3tb'
        self.laptop['gpu'] = 'RTX5090'
        return self
    
    def with_cpu(self,cpu):
        self.laptop['cpu'] = cpu
        return self
    
    def build(self):
        return self.laptop.copy()
    
print(LaptopBuilder().for_study().with_cpu('ryzen 9 9900x3d').build())

# prototype
import copy
template_order = {
    'devilery':'standart',
    'promo':False,
    'items':['books']
}
fast_order = copy.deepcopy(template_order)
fast_order['devilery']='express'

print(template_order,fast_order)

# structure pattern
# Adapter
class OldSmsService:
    def send_sms(self,phone,text):
        print(f'old service:{phone},:{text}')

class SmsAdapter:
    def __init__(self,service,phone):
        self.service =service
        self.phone = phone

    def send(self,message):
        self.service.send_sms(self.phone,message)

SmsAdapter(OldSmsService(),'+79999999999').send('Message')

# Bring
class TV:
    def turn_on(self):
        return 'TV is on'
class Radio:
    def turn_on(self):
        return 'Radio is on'

class RemoveControl:
    def __init__(self,device):
        self.device = device
    def power(self):
        self.device.turn_on()
print(RemoveControl(TV().power()))


class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
class Folder:
    def __init__(self,name):
        self.name = name
        self.children = []
    def add(self,child):
        self.children.append(child)
    
    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
docs = Folder('docx')
docs.add(File('text_1.txt',10))
docs.add(File('text_2.txt',20))

# Decorator
class Coffee:
    def price(self):
        return 120
    def desciption(self):
        return 'Coffee'

class MilkDecorator:
    def __init__(self,drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 30
    
    def description(self):
        return self.drink.description() + ',milk'
    
class SypupDecorator:
    def __init__(self,drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 25
    
    def description(self):
        return self.drink.description() + ',sypup'
    
drink = SypupDecorator(MilkDecorator(Coffee()))
print(drink.price(),drink.description())

# Facade
class PaymentService:
    def pay(self,amount):
        print(f'Pay {amount} confirmed')
class WarehouseService:
    def pay(self,item):
        print(f'Item {item} confirmed')
class DeliveryService:
    def create(self,item):
        print(f'delivery for {item} created')
class OrderFacade:
    def __init__(self):
        self.payment = PaymentService()
        self.warehouse = WarehouseService()
        self.delivery = DeliveryService()
    def place_order(self,item,amount):
        self.payment.pay(amount)
        self.warehouse.reserve(item)
        self.delivery.create(item)
        print('order completed')

OrderFacade().place_order('Headphone',8932)

# Flyweight

class Flyweight:
    def __init__(self,color):
        self.color = color
    def draw(self,x,y):
        print(self.color,x,y)

class Factory:
    _cached = {}
    def get(cls,color):
        if color not in cls._cached:
            cls._cached[color] = Flyweight(color)
        return cls._cached[color]

red1 = Factory.get('red')
red2 = Factory.get('red')
print(red1 is red2)

# proxy
class Image:
    def __init__(self,path):
        print('Loading')
        self.path = path

    def show(self):
        print(f'show {self.path}')

class ImageProxy:
    def __init__(self,path):
        self.path =path
        self._real = None

    def show(self):
        if self._real is None:
            self._real = Image(self.path)
        self._real.show()

img = Image('photo.png')
img.show() 
img.show

# Поведенческие паттерны
# chain of responsibility

class Handler:
    def __init__(self,next_handler = None):
        self.next_handler = next_handler

    def handle(self,request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return 'Unhandled'
class AuthHandler(Handler):
    def handle(self,request):
        if not request.get('user'):
            return '404 Unautorized'
        return super().handle(request)
class RoleHandler(Handler):
    def handle(self, request):
        if request.get('role') != 'admin':
            return '403 Forbidden'
        return super().handle(request)
    
chain = AuthHandler(RoleHandler())
print(chain.handle({'user':'alice','role':'admin'}))

# command 
class Light:
    def on(self):
        print('Light is on')

class TurnOnCommand:
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.on()

class Button:
    def __init__(self,command):
        self.command = command

    def press(self):
        self.command.execute()

Button(TurnOnCommand(Light())).press()

# Mediator
class ChatMediator:
    def send(self,message,user):
        for c in user.colleagues:
            if c is not user:
                c.receive(message)

class User:
    def __init__(self,name,mediator):
        self.name = name
        self.mediator = mediator
        self.colleagues = []

    def send(self,message):
        self.mediator.send(f'{self.name}:{message}',self)
    
    def receive(self, message):
        print(message)
        
mediator = ChatMediator()
alice = User('Alice',mediator)
bob = User('Bob',mediator)
alice.colleagues = ['alice','bob']
bob.colleagues = ['alice','bob']
alice.send('Hello')

# MEmento



class Editor:
    def __init__(self):
        self.text = ''
    def write(self,text):
        self.text += text

    def save(self):
        return self.text
    
    def restore(self,snapshot):
        self.text = snapshot

editor = Editor()
editor.write('Hello')
snapshot = editor.save()
editor.write(', World')
print(editor.text)
editor.restore(snapshot)
print(editor.text)

# Observer

class Order:
    def __init__(self):
        self.subscribers = []

    def subscribe(self,listener):
        self.subscribers.append(listener)

    def set_status(self,status):
        for subscrider in self.subscribers:
            subscrider(status)

def email_listener(status):
    print(f'Email:Change of status to {status} has been made')

def sms_listener(status):
    print(f'SMS:Change of status to {status} has been made')

order = Order()
order.subscribe(email_listener)
order.subscribe(sms_listener)
order.set_status('devilery')


# State

class DraftState:
    def publish(self,document):
        document.state = ReviewState()
        return 'asoiafj'
class ReviewState:
    def publish(self,document):
        document.state = PublishedState()
        return 'document published'

class PublishedState:
    def publish(self,document):
        return 'published already'
    
class Document:
    def __init__(self):
        self.state = DraftState()

    def publish(self):
        return self.state.publish(self)

doc = Document()
doc.publish()
doc.publish()
doc.publish()

# strategy
class StandardStrategy:
    def calculate(self,weight):
        return 200 + weight * 10

class ExpressDelivery:
    def calculate(self,weight):
        return 500 + weight * 20
    
class PickupDelivery:
    def calculate(self,weight):
        return 0
    
class DeliveryCalc:
    def __init__(self,strategy):
        self.strategy = strategy

    def get_price(self,weight):
        return self.strategy.calculate(weight)


# Tempalte method

class ReportTemplate:
    def build(self):
        data = self.fetch_data()
        return self.format_data(data)
    
    def fetch_data(self):
        raise NotImplementedError
    
    def format_data(self,data):
        raise NotImplementedError
    
class SalesReport(ReportTemplate):
    def fetch_data(self):
        return [100,200,300]
    
    def format_data(self, data):
        return f'sum of sales:{sum(data)}'
    
print(SalesReport().build())

# Visitor 

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def accept(self,visitor):
        return visitor.visit_book(self)
    
    
class Course:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def accept(self,visitor):
        return visitor.visit_course(self)
    
class DiscountVisitor:
    def visit_book(self,book):
        return f'{book.title}: {book.price * 0.9}'
    
    def visit_course(self,course):
        return f'{course.title}: {course.price * 0.2}'
    
visitor = DiscountVisitor()
items = [Book('book',1000),Course('course',5000)]
for item in items:
    print(item.accept(visitor))