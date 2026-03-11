# def uppercase_name(name:str) -> str:
#     return name.upper()

# 3
# course_title: str = 'sfdoew'
# students_count: int = 20
# is_open: bool = True

# class Employee:
#     company: str = 'Tech'

#     def __init__(self, emp_id:int,name:int,salary:int) -> None:
#         self.emp_id:int = emp_id
#         self.name:int = name
#         self.salary:int = salary
        
# # 4
# names: list[str] = ["Alice",'BOB']
# salaries: dict[str,int] = {'Alice':1010,'Bob':2019}
# user_pair: tuple[str,int] = ('Alice',1)
# permissions: set[str] = {'read','write'}

# # 5
# from typing import Any

# def stringfy(value:Any)->str:
#     return str(value)

# # 6
# from typing import Optional,Union
# def find_emp_name(emps:dict[int,str],emp_id: int) -> Optional[str]:
#     return emps.get(emp_id)

# def parse_emp_id(raw:Union[str,int]) -> int:
#     return int(raw)

# # 7
# from typing import Sequence,Mapping,Iterable

# def print_names(items: Iterable[str])-> None:
#     for item in items:
#         print(item)

# def first_two(items: Sequence[str]) -> list[str]:
#     return list(items[:2])

# def get_salary(data:Mapping[str,int],name: str) -> int:
#     return data[name]

# 8
from typing import Callable

def app_f(text:str,formatter:Callable[[str],str])-> str:
    return formatter(text)

# 9
# EmployeeId = int
# SalaryMap = dict[str,int]
# TagList  = list[str]

# emp_id: EmployeeId = 20
# skills: TagList = ['tag']

# # 
# from typing import TypedDict

# class Employee(TypedDict):
#     emp_id: int
#     name: str
#     salary: int

# payload: Employee = {'emp_id':1,'name':'Alice','salary':1000}

# 11
from dataclasses import dataclass

class Employee_card:
    emp_id: int
    name: str

card = Employee_card(emp_id = 1,name = 'Alice')

def find_emp(emps:dict[int,Employee_card]) -> None:
    pass
