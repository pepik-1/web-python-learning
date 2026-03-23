staff_data = [
    ("Employee", "Алиса", 2000),
    ("Manager", "Боб", 2500, 800),
    ("Sales", "Кира", 1800, 12000),
    ("Employee", "Данил", 2200),
    ("Sales", "Ева", 1700, 7000)
]


class Employee:
    def __init__(self,name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # TODO: реализовать __init__(name, base_salary)
    # сохранить self.name и self.base_salary
    def monthly_income(self):
        return self.base_salary

    # TODO: реализовать monthly_income()
    # вернуть доход за месяц обычного сотрудника: base_salary
    


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    # TODO: реализовать __init__(name, base_salary, bonus)
    # вызвать super().__init__(...) и сохранить self.bonus

    def monthly_income(self):
        return self.base_salary + self.bonus
    # TODO: переопределить monthly_income()
    # вернуть доход менеджера: base_salary + bonus
    


class Sales(Employee):
    def __init__(self, name, base_salary, sales_amount):
        super().__init__(name, base_salary)
        self.sales_amount = sales_amount
    # TODO: реализовать __init__(name, base_salary, sales_amount)
    # вызвать super().__init__(...) и сохранить self.sales_amount


    def monthly_income(self):
        return self.base_salary + self.sales_amount * 0.05

    # TODO: переопределить monthly_income()
    # вернуть доход sales: base_salary + sales_amount * 0.05
    pass


def calculate_total_income(staff):
    total = 0
    for person in staff:
        total += person.monthly_income()

    # TODO: пройти по staff и для каждого person добавить person.monthly_income() в total
    return total


staff = []
for row in staff_data:
    role = row[0]
    name = row[1]
    base_salary = row[2]
    
    if role == "Employee":
        obj = Employee(name, base_salary)
    elif role == "Manager":
        bonus = row[3]
        obj = Manager(name, base_salary, bonus)
    elif role == "Sales":
        sales_amount = row[3]
        obj = Sales(name, base_salary, sales_amount)
    
    staff.append(obj)

    # TODO:
    # если role == "Employee": Employee(name, base_salary)
    # если role == "Manager": Manager(name, base_salary, bonus)
    # если role == "Sales": Sales(name, base_salary, sales_amount)
    # добавить созданный объект в staff
    pass


for person in staff:
    print(person.name)
    print(person.monthly_income())

    # TODO: вывести person.name и person.monthly_income()
    pass

print("Общий фонд:", calculate_total_income(staff))
