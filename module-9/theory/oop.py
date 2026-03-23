from abc import ABC, abstractmethod
class EmployeeBase(ABC):
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name
    @abstractmethod
    def compensation(self):
        pass


class Employee(EmployeeBase):
    company = 'pepik_persona_228'
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self._salary = 0

    def __str__(self):
        return f'{self.name}: {self.salary}'
    
    def __eq__(self,other):
        if not isinstance(other,Employee):
            return NotImplemented
        return self.emp_id == other.emp_id
    
    def __lt__(self, other):
        if not isinstance(other,Employee):
            return NotImplemented
        return self.emp_id < other.emp_id

    def info(self):
        return f'{self.name} ---->  {self.salary}'
    
    @classmethod
    def from_string(cls,raw):
        emp_id,name,salary = raw.split(',')
        return cls(int(emp_id),name,int(salary))
    
    @staticmethod
    def valid_name(name):
        return len(name.strip()) >= 2
    
    def get_salary(self):
        return self.salary
    def set_salary(self,value):
        if value <0:
            self.salary = 0
        else:
            self.salary = value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        self._salary = value

    @salary.deleter
    def salary(self):
        self._salary = 0

    def yearly_income(self):
        return self.salary * 12
    def compensation(self):
        return self.salary
    

class LogableMixin:
    def log(self,message):
        print(f'[LOG] {self.name}: {message}')



class Manager(Employee,LogableMixin):
    def __init__(self,emp_id,name,salary,bonus):
        super().__init__(emp_id,name,salary)
        self.bonus = bonus
    def yearly_income(self):
        return super().yearly_income() + self.bonus
    
    
mm = Manager(3,'alexey',2342,35153)
print(mm.yearly_income())
print(Manager.__mro__)
print(mm.log('1232141523'))

m1 = Manager(3,'yeeeeeeyyyy',12341,523)
m2 = Manager(4,'aaaaaiiioooo',21535,366424)
print(m1 == m2)

# e = Employee(1, 'pepik', 999999999999999)
# print(e.name,Employee.company)
# print(e.info())
# m = Employee.from_string('2,ewfwaaw,43252523')
# print(m.emp_id,m.name,m.salary)
# p = Employee.valid_name(m.name)
# print(p)

# m.set_salary(4000)
# print(m.get_salary(),m.salary)
# m.salary = 4000
# print(m.salary)
# del m.salary
# print(m.salary)