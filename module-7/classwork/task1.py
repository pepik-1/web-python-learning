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
goods_in = {}
goods_out = {}
dates = []
minus = ''

for operation in operations:
    date,product,operation_type,quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]
    summ = summ + int(quantity)

    if operation['product'] == 'яблоко':
        dates.append(operation['date'])





    # 3
    goods_in.setdefault(product,int())
    goods_out.setdefault(product,int())
    if operation_type == 'IN':
        goods_in[product] = goods_in[product] + int(quantity)
        
    else:
        goods_out[product] = goods_out[product]+ int(quantity)
    
    
    

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
            minus = el

    # 4.2
    if operation_type == 'IN':
            products_in.append(product)

print(summ, count_in, count_out, summa)

for operation in operations:
    date,product,operation_type,quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]
    if product not in products_in:
        only_out.append(product)

print(goods_in,goods_out)

max_in_product = None
max_in_quantity = -1
for product,quantity in goods_in.items():
    if quantity > max_in_quantity:
        max_in_product = product
        max_in_quantity = quantity
print(max_in_product,max_in_quantity)

max_out_product = None
max_out_quantity = -1
for product,quantity in goods_out.items():
    if quantity > max_out_quantity:
        max_out_product = product
        max_out_quantity = quantity
print(max_out_product,max_out_quantity)

print(dates)

with open('report.txt','w',encoding='utf-8') as file:

    file.write('ОТЧЁТ ПО СКЛАДУ\n')
    file.write(f'Итоговые остатки: {summa}\n')
    file.write(f'Общее поступление: {goods_in}\n')
    file.write(f'Общая отгрузка: {goods_out}\n')
    file.write(f'Товары с отрицательным остатком:{minus}\n')
    file.write(f'Товары без поступлений, но с отгрузкой:{only_out}\n')
    file.write(f'Товар с максимальным поступлением: {max_in_product}\n')
    file.write(f'Товар с максимальной отгрузкой:{max_out_product}\n')
    file.write(f'Даты операций с яблоком:{dates}\n')

print(operations)