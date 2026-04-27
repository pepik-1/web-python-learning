# s = single responsibility
# Bad example
class BadReport:
    def __init__(self,title,rows):
        self.title = title
        self.rows = rows
    
    def as_text(self):
        lines = [self.title,'-'*len(self.rows)]
        for row in self.rows:
            lines.append(f'{row['name']}:{row['value']}')
        return '\n'.join(lines)
    def save(self,filename):
        with open(filename,'w',encoding='utf-8')as file:
            file.write(self.as_text())
    
# Good example
from dataclasses import dataclass

@dataclass
class Report:
    title:str
    rows:list[dict]

class TextReportFormat:
    def format(self,report:Report) -> str:
        lines = [report.title,'-' * len(report.rows)]
        for row in report.rows:
            lines.append(f'{row['name']}: {row['value']}')
        return '\n'.join(lines)
    
class FileStorage:
    def save(self,filename:str,content:str)-> None:
        with open(filename,'w',encoding='utf-8')as file:
            file.write(content)

report = Report('sales',[{'name':'Books','value':100}])
print(TextReportFormat().format(report))

# o - Open/Closed

# Bad example
def calculate_discount_bad(customer_type:str,amount:float) -> float:
    if customer_type == 'regular':
        return amount * 0.05
    if customer_type == 'vip':
        return amount * 0.15
    if customer_type == 'customer':
        return amount * 0.30
    return 0

print(calculate_discount_bad('regular',10000))

# good example

from typing import Protocol

class Discount(Protocol):
    def discount_for(self,amount:float)->float:
        ...

class RegularDiscount:
    def discount_for(self,amount:float)->float:
        return amount * 0.05

class VipDiscount:
    def discount_for(self,amount:float)->float:
        return amount * 0.15

class NoDiscount:
    def discount_for(self,amount:float)->float:
        return 0

def final_price(amount: float,discount:Discount) -> float:
    return amount - discount.discount_for(amount)

# L - Liskov Substitution
# Bad example

class BadBird:
    def fly(self):
        print('Flying')
    
class BadSparrow(BadBird):
    pass

class BadPinguin(BadBird):
    def fly(self):
        raise ValueError('pinguin can`t fly')

def make_bird_fly(bird:BadBird):
    bird.fly()

try:
    make_bird_fly(BadPinguin())
except ValueError as e:
    print('Error:',e)

# Good example
from dataclasses import dataclass
from typing import Protocol

@dataclass
class Bird:
    name:str

class Flyable:
    def fly(self) -> None:
        ...
class Sparrow(Bird):
    def fly(self):
        print(f'{self.name} flying')

class Penguin(Bird):
    def swim(self):
        print(f'{self.name} swimming')

def make_fly(obj:Flyable):
    obj.fly()

make_fly(Sparrow('Sparrow'))
Penguin('Penguin').swim()

# I - Interface Segregation

# Bad example

from abc import ABC, abstractmethod

class BadDeviceOffice(ABC):
    @abstractmethod
    def print_document(self,text:str) -> None:
        pass
    @abstractmethod
    def scan_document(self) -> None:
        pass
    @abstractmethod
    def send_fax(self,phone:str,text:str) -> None:
        pass

class Printer(BadDeviceOffice):
    def print_document(self, text:str)->None:
        print('Print:',text)

    def scan_document(self)->None:
        raise NotImplementedError('printer isn`t scaning')
    
    def sand_fax(self,phone:str,text:str)->None:
        raise NotImplementedError('printer isn`t sending fax')
    
# Good Example
from typing import Protocol

class Printer(Protocol):
    def scan_document(self,text:str)->None:
        ...

class Scanner(Protocol):
    def scan_document(self,text:str)->None:
        ...

class LPrinter:
    def print_document(self,text:str) -> None:
        print('document printing')
    
class MFPrinter:
    def print_document(self,text:str) -> None:
        print('document printing')

    def scan_document(self,text:str) ->str:
        return 'Scan is ready'
    
def print_document(device: Printer):
    device.print_document('document')

def scran_document(device:Scanner):
    device.scan_document()

print_document(LPrinter())
print_document(MFPrinter())
print(scran_document(MFPrinter()))

# D - Dependency Invention

# Bad example

class EmailSender:
    def send(self,email:str,message:str) -> None:
        print(f'Email for {email}:{message}')

class BadOrderService:
    def __init__(self):
        self.sender = EmailSender()

    def complete_order(self,email:str,total:float)-> None:
        print(f'order with {total} cost ordered')

BadOrderService().complete_order('user@example.com',3500)

# Good example
from typing import Protocol

class Notifier(Protocol):
    def send(self,contact:str,message:str) -> None:
        ...
class EmailNotifier:
    def send(self,contact:str,message:str) -> None:
        print(f'Email for {contact}:{message}')

class BadOrderService:
    def __init__(self):
        self.sender = EmailSender()
