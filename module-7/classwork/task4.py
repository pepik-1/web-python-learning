lines = [
    "2026-02-01,IT,Иванов,Ноутбук,1,approved",
    "2026-02-01,HR,Петрова,Клавиатура,2,pending",
    "2026-02-02,Finance,Сидоров,Монитор,1,approved",
    "2026-02-02,IT,Кузнецов,Мышь,3,rejected",
    "2026-02-03,IT,Иванов,Док-станция,1,rejected",
    "2026-02-03,HR,Петрова,Гарнитура,1,approved",
    "2026-02-04,Finance,Сидоров,Клавиатура,1,pending",
    "2026-02-04,IT,Смирнов,Монитор,2,approved"
]

requests = []
# список заявок
# каждый элемент: dict с ключами
# date, department, employee, category, quantity, status

department_stats = {}
# department -> {"total": 0, "approved": 0, "pending": 0}

all_categories = set()
# множество уникальных категорий оборудования

employee_statuses = {}
# employee -> set статусов сотрудника

category_quantity = {}
# category -> суммарное количество запрошенных единиц

mixed_status_employees = []
# сотрудники, у которых есть и approved, и rejected


with open("equipment_requests.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(f'{line}\n')

    # TODO: записать строки lines в файл
    pass


with open("equipment_requests.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        # date, department, employee, category, quantity, status
        date, department, employee, category, quantity, status = line.split(',')
        requests.append({
            'date':date,
            'department':department,
            'employee':employee,
            'category': category,
            'quantity':int(quantity),
            'status':status
        })
        # TODO:
        # 1) разбить строку по ','
        # 2) преобразовать quantity в int
        # 3) создать словарь заявки
        # 4) добавить словарь в requests
        pass

for el in requests:
    if el['department'] not in department_stats:
        department_stats[el['department']] = {'total':0,'approved':0,'pending':0}
    department_stats[el['department']]['total'] +=1
    if el['status'] == 'approved':
        department_stats[el['department']]['approved']+=1
    if el['status'] == 'pending':
        department_stats[el['department']]['pending']+=1

for el in requests:
    if el['category'] not in all_categories:
        all_categories.add(el['category'])

for el in requests:
    if el['employee'] not in 


for request in requests:
    # TODO:
    # получить department, employee, category, quantity, status

    # 1) обновить department_stats
    # 2) добавить category в all_categories
    # 3) обновить employee_statuses
    # 4) обновить category_quantity
    pass


for employee, statuses in employee_statuses.items():
    # TODO:
    # если у сотрудника есть одновременно approved и rejected
    # добавить employee в mixed_status_employees
    pass

top_category = None
top_quantity = 0

# TODO:
# пройти по category_quantity и найти категорию
# с максимальным суммарным количеством


with open("equipment_report.txt", "w", encoding="utf-8") as file:
    # TODO:
    # записать в файл:
    # - статистику по отделам
    # - список категорий
    # - сотрудников с mixed-статусами
    # - самую востребованную категорию
    pass
