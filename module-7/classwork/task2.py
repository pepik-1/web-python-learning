logs = ['2026-02-01,Иван,ENTER',
'2026-02-01,Мария,ENTER',
'2026-02-01,Иван,EXIT',
'2026-02-01,Иван,EXIT',
'2026-02-01,Олег,EXIT',
'2026-02-02,Мария,EXIT',
'2026-02-02,Олег,ENTER',]

with open('passages.txt','w',encoding='utf-8') as f:
    for el in logs:
        f.write(f'{el}\n')

operations = []

with open('passages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        date,name,action = line.split(',')
        operations.append({'date':date,'name':name,'action':action})


enter_count = {}
exit_count = {}
enter_exit = {}
bad_people = []
error_row = []

for operation in operations:
    

    if operation['action'] == 'ENTER\n':
        enter_count.setdefault(operation['name'],0)
        enter_count[operation['name']] = enter_count.get(operation['name'],0)+1
    if operation['action'] == 'EXIT\n':
        exit_count.setdefault(operation['name'],0)
        exit_count[operation['name']] = exit_count.get(operation['name'],0)+1
        
    enter_exit.setdefault(operation['name'],list()).append(operation['action'])
    



for el in enter_exit:
    if enter_exit[el][-1] == 'EXIT\n':
        bad_people.append(el)


for key,value in enter_exit.items():
    n = len(value)
    for el in value:
        if el == el[n-1]:
            error_row.append(key)
print(error_row)
