logs = ['2024-01-01,яблоко,IN,50',
'2024-01-02,банан,IN,30',
'2024-01-03,яблоко,OUT,10',
'2024-01-03,груша,OUT,5',
'2024-01-04,груша,IN,20',
'2024-01-05,банан,OUT,40',
'2024-01-06,яблоко,OUT,5',
'sdadas,affsa,OUT,32']


with open('inventory.txt','w', encoding="utf-8") as f:
    for el in logs:
        f.write(f'{el}\n')

operations = []

with open('inventory.txt', 'r',encoding='utf-8') as file:
    summ = 0
    for line in file:
        date,product,operation_type,quantity = line.split(",")
        operations.append({ "date": date,"product": product,"operation_type": operation_type,"quantity": quantity})

summ = 0
count_in = 0
count_out = 0
summa = {}
products_in = []
only_out = []

for operation in operations:
    date,product,operation_type,quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]
    summ = summ + int(quantity)

    # 3
    if operation_type == 'IN':
        count_in = count_in+1
    else:
        count_out = count_out+1

    # 3.1
    if product not in summa:
        summa.setdefault(product,int(),)
    if operation_type == 'IN':
        summa[product] = summa[product] + int(quantity)
    if operation_type == 'OUT':
        summa[product] = summa[product] - int(quantity)

    

    # 4.1
    for el in summa:
        if summa[el] < 0:
            print(el)

    # 4.2
    if operation_type == 'IN':
            products_in.append(product)

print(summ, count_in, count_out, summa)

for operation in operations:
    date,product,operation_type,quantity =  date,product,operation_type,quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]
    if product not in products_in:
        only_out.append(product)

print(only_out)

            
            