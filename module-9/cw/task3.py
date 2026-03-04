from abc import ABC, abstractmethod

staff_rows = [
    ("Developer", "Алиса", 2200, "Engineering", 12, 25),
    ("Manager", "Боб", 2800, "Engineering", 900),
    ("Analyst", "Кира", 2000, "Data", 14, 40),
    ("Developer", "Данил", 2400, "Engineering", 4, 25),
    ("Manager", "Ева", 2600, "Data", 600),
    ("Analyst", "Жан", 1900, "Operations", 20, 30),
]


class EmployeeBase(ABC):
    def __init__(self,name,base_salary,department):
        self.name = name
        self.base_salary = base_salary
        self.department = department
    
    def short(self):
        return f'{self.name} {self.department}'
    # TODO: __init__(name, base_salary, department)
    # TODO: short() -> строка "Имя (Department)"

    @abstractmethod
    def total_pay(self):
        pass
    
    def __repr__(self):
        return f'{self.name}(name={self.name},{self.department})'
    

    def __lt__(self, other):
        if not isinstance(self,other):
            return NotImplemented
        
        return self.total_pay() < other.total_pay()



    # TODO: __repr__
    # TODO: __lt__(other) -> сравнение по total_pay()


class Developer(EmployeeBase):
    def __init__(self, name, base_salary, department, overtime_hours, overtime_rate):
        super().__init__(name, base_salary, department)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate
    def total_pay(self):
        return self.base_salary + self.overtime_rate * self.overtime_hours

    # TODO: __init__(name, base_salary, department, overtime_hours, overtime_rate)
    # TODO: total_pay()
    


class Manager(EmployeeBase):
    def __init__(self, name, base_salary, department,bonus):
        super().__init__(name, base_salary, department)
        self.bonus = bonus
    def total_pay(self):
        return self.base_salary + self.bonus
    

    # TODO: __init__(name, base_salary, department, bonus)
    # TODO: total_pay()
    


class Analyst(EmployeeBase):
    def __init__(self, name, base_salary, department,reports_done, report_rate):
        super().__init__(name, base_salary, department)
        self.reports_done = reports_done
        self.report_rate = report_rate
    def total_pay(self):
        return self.base_salary + self.reports_done * self.report_rate


    # TODO: __init__(name, base_salary, department, reports_done, report_rate)
    # TODO: total_pay()
    



class DepartmentBudget:
    employees = {}
    def __init__(self, department_name):
        self.department_name = department_name
    
    def add_employee(self,emp):
        for el in staff_rows:
            if el[1] not in self.employees:
                self.employees.setdefault(el[1],0)
                self.employees[el[1]] = self.employees.get(el[1],0) + el[2]
    
    def department_total(self):
        department = {}
        for el in staff_rows:
            if el[1] not in department:
                department.setdefault(el[3],0)
                department[el[3]] = department.get(el[3],0) + el[2]

    def top_paid(self):
        return max(self.employees)



    # TODO: __init__(department_name)
    # TODO: add_employee(emp)
    # TODO: department_total()
    # TODO: top_paid()
    


class PayrollService:
    def __init__(self,employees):
        self.employees = employees
        

    def total_company_payroll(self):
        return sum(emp.total_pay() for emp in employees) 

    
    def totals_by_department(self):
        departments = {}
        for el in staff_rows:
            departments.setdefault(el[3],0)
            departments[el[3]] = departments.get(el[3],0) + el[2]
        return departments
        
    def highest_paid_employee(self):
        employees = {}
        for el in staff_rows:
            if el[1] not in self.employees:
                self.employees.setdefault(el[1],0)
                self.employees[el[1]] = self.employees.get(el[1]) + el[2]
        
        max_s_emp = ''
        max_salary = 0
        for emp,salary in employees:
            if salary > max_salary:
                max_s_emp = emp

        return max_s_emp
    

    # TODO: __init__(employees)
    # TODO: total_company_payroll()
    # TODO: totals_by_department()
    # TODO: highest_paid_employee()
    
employees = []
for el in staff_rows:
    role = el[0]
    if role == 'Developer':
        emp = Developer(el[1],el[2],el[3],el[4],el[5])
        employees.append(emp)
    if role == 'Manager':
        emp = Manager(el[1],el[2],el[3],el[4])
        employees.append(emp)
    if role == 'Analyst':
        emp = Analyst(el[1],el[2],el[3],el[4],el[5])
        employees.append(emp)


payroll = PayrollService(employees)
print(payroll.total_company_payroll())



# TODO: создать объекты сотрудников из staff_rows
# TODO: создать PayrollService и вывести общий payroll
# TODO: вывести суммы по отделам
# TODO: вывести самого высокооплачиваемого сотрудника

