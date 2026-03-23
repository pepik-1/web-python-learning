lines = [
    "SHP-1001,North,Chicago,3,3,40,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1003,East,Miami,2,2,35,cancelled",
    "SHP-1004,East,Chicago,5,8,15,delivered",
    "SHP-1005,West,Dallas,1,1,50,delivered",
    "SHP-1006,West,Miami,2,4,30,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1007,South,Atlanta,6,6,25,in_transit",
    "SHP-1008,South,Dallas,3,5,10,delivered"
]

deliveries = []
# список словарей с записями доставок
# ключи: shipment_id, warehouse, city, planned_day, actual_day, items, status

warehouse_stats = {}
# warehouse -> {"total": 0, "delayed": 0}

cities = set()
# множество городов доставки

shipment_counter = {}
# shipment_id -> количество встреч

duplicate_shipments = []
# список shipment_id, которые дублируются

city_delivered_items = {}
# city -> суммарное количество items для status == delivered


with open("delivery_log.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(f'{line}\n')


with open("delivery_log.txt", "r", encoding="utf-8") as file:
    
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        shipment_id,warehouse ,city = parts[0] , parts[1],parts[2]
        planed_day = int(parts[3])
        actual_day = int(parts[4])
        items = int(parts[5])
        status = parts[6]
        deliveries.append({
            'shipment_id' : shipment_id,
            'warehouse': warehouse,
            'city':city,
            'planed_day':planed_day,
            'actual_day':actual_day,
            'items':items,
            'status':status
        
        })
        # TODO:
        # 1) разбить строку по ','
        # 2) planned_day, actual_day, items перевести в int
        # 3) собрать словарь и добавить его в deliveries
        pass

for el in deliveries:
    if el['warehouse'] not in warehouse_stats:
        warehouse_stats[el['warehouse']] = {'total':0,'delayed':0}
    warehouse_stats[el['warehouse']]['total'] += 1

    if el['planed_day'] < el['actual_day']:
        warehouse_stats[el['warehouse']]['delayed'] += 1


for el in deliveries:
    if el['city'] not in cities:
        cities.add(el['city'])

for el in deliveries:
    shipment_counter.setdefault(el['shipment_id'],0)
    shipment_counter[el['shipment_id']] = shipment_counter.get(el['shipment_id'],0) +1
for shipment_id,count in shipment_counter.items():
    if count > 1:
        duplicate_shipments.append(shipment_id)

for el in deliveries:
    city_delivered_items.setdefault(el['city'],0)
    if el['status'] == 'delivered':
        city_delivered_items[el['city']] = city_delivered_items.get(el['city'],0) + el['items']

# warehouse_delayed = {}
# for el in deliveries:
#     warehouse_delayed.setdefault(el['warehouse'],0)
#     if el['planed_day'] < el['actual_day']:
#         warehouse_delayed[el['warehouse']] = warehouse_delayed.get(el['warehouse'],0) + 1
# delayed_max = 0
# for warehouse,delayed in warehouse_delayed.items():
#     if delayed > delayed_max:
#         delayed_max = delayed
# for warehouse, delayed in warehouse_delayed.items():
#     if delayed_max == delayed:
#         print(warehouse)



for delivery in deliveries:
    # TODO:
    # получить shipment_id, warehouse, city, planned_day, actual_day, items, status

    # 1) обновить warehouse_stats
    # 2) если actual_day > planned_day, увеличить delayed
    # 3) добавить city в cities
    # 4) обновить shipment_counter
    # 5) если status == delivered, обновить city_delivered_items
    pass


for shipment_id, count in shipment_counter.items():
    # TODO:
    # если count > 1, добавить shipment_id в duplicate_shipments
    pass

worst_warehouse = None
max_delay_rate = -1
for warehouse,stat in warehouse_stats.items():
    delay_rate = stat['delayed'] / stat['total']
    if delay_rate > max_delay_rate:
        max_delay_rate = delay_rate
        worst_warehouse = warehouse
print(worst_warehouse)


# TODO:
# пройти по warehouse_stats
# для каждого склада посчитать delay_rate = delayed / total
# найти склад с максимальным delay_rate


with open("delivery_report.txt", "w", encoding="utf-8") as file:
    file.write(f'warehouse stat: {warehouse_stats}\n')
    file.write(f'cityis list: {cities}\n')
    file.write(f'dublicates: {duplicate_shipments}\n')
    file.write(f'worst warehouse: {worst_warehouse}\n')
    file.write(f'all: {city_delivered_items}\n')

    # TODO:
    # записать в отчет:
    # - статистику по складам
    # - список городов
    # - дубликаты shipment_id
    # - склад с максимальным процентом просрочек
    # - доставленные объёмы по городам
    pass
