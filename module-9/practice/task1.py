employees_data = [
    (101, "Алиса", 1800, "Data"),
    (102, "Боб", 2200, "Backend"),
    (103, "Кира", 1600, "QA"),
    (104, "Данил", 2500, "Backend")
]


class Employee:
    def __init__(self,emp_id,name,salary,department):
        self.emp_id = emp_id
        self.name = name
        self._salary = salary
        self.department = department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            self._salary = 0
        else:
            self.salary = value

    def raise_salary(self,persent):
        self._salary = self._salary * (1 + persent/100)

    def to_dict(self):
        return{
            'emp_id':self.emp_id,
            'name':self.name,
            'salary':self.salary,
            'department':self.department
        }
    



    # TODO: реализовать __init__
    # TODO: реализовать property salary (getter/setter с валидацией)
    # TODO: увеличить salary на percent процентов
    # новая salary = salary * (1 + percent / 100)
    # TODO: вернуть dict: {"emp_id": ..., "name": ..., "salary": ..., "department": ...}
    pass


class EmployeeRegistry:
    def __init__(self):
        self._employees = {}

    def add_employee(self, employee):
        self._employees[employee.emp_id] = employee
        

    def remove_employee(self, emp_id):
        self._employees.pop(emp_id)
        

    def find_by_department(self, department):
        return [emp for emp in self._employees.values() if emp.department == department]
        

    def total_payroll(self):
        return sum(emp.salary for emp in self._employees.values())
        


registry = EmployeeRegistry()

for emp_id, name, salary, department in employees_data:
    employee = Employee(emp_id,name,salary,department)
    registry.add_employee(employee)

registry._employees[101].raise_salary(10)
registry._employees[103].raise_salary(5)

# TODO: повысить зарплату Алисе на 10%
# TODO: повысить зарплату Кире на 5%

print("Всего сотрудников:", len(registry._employees))
print("ФОТ:", registry.total_payroll())
print("Backend:", [e.name for e in registry.find_by_department("Backend")])
