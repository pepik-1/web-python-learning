rows = [
    'S-100,Acme,12.5,express,RU',
    'S-101,Beta,0,standard,RU',
    'S-102,Acme,abc,vip,KZ',
    'S-103,Delta,8.5,urgent,BY',
    'S-104,Gamma,15,vip,UZ',
    'S-105,Acme,4.0,standard,KZ',
    'S-106,Beta,9.5,express,BY',
]


class ShipmentError(Exception):
    pass


class RowFormatError(ShipmentError):
    pass


class WeightError(ShipmentError):
    pass


class PriorityError(ShipmentError):
    pass


class RegionError(ShipmentError):
    pass


def parse_shipment(row):
    shipment_id,client,weight,priority,region = row.split(',')
    # TODO: распарсить строку и провалидировать weight, priority, region
    # TODO: при ошибке конвертации weight использовать raise ... from ...
    try:
        row.split(',') == 5
    except ValueError:
        raise RowFormatError('Wrong row format error')
    
    try:
        weight = float(weight)
        if weight < 0:
            raise WeightError('wrong weight')
    except ValueError:
        raise WeightError('weight must be num')

    priorities = { 'standard', 'express', 'vip'}

    try:
        if priority not in priorities:
            raise PriorityError('unknown priority')
    except ValueError as e:
        raise PriorityError('unknown priority') from e
    
    regions = {'RU', 'KZ', 'BY'}
    try:
        if region not in regions:
            raise RegionError('unknown region') 
    except ValueError as e:
        raise RegionError('unknown region') from e
    
    
    return {'shipment_id':shipment_id,'client':client,'weight':weight,'priority':priority,'region':region}


def load_shipments(rows):
    shipments = []
    errors = []
    for row in rows:
        try:
            result = parse_shipment(row)
            shipments.append(result)
        except ShipmentError as e:
            errors.append((row,type(e).__name__,e))
    return shipments,errors

shipments,errors = load_shipments(rows)
print(len(shipments))
print(len(errors))

err_types = {}
for row,err,_ in errors:
    err_types.setdefault(err,list()).append(row)
print(err_types)
    
sum_weight = 0
for el in shipments:
    if el['priority'] == 'express' or 'vip':
        sum_weight += el['weight']
print(sum_weight)

we_leader = {}
for el in shipments:
    we_leader.setdefault(el['client'],0)
    we_leader[el['client']] += el['weight']

res = ''
numb = 0
for client, num in we_leader.items():
    if num > numb:
        numb = num
        res = client
print(res)



# TODO: вызвать load_shipments(rows)
# TODO: вывести число валидных отгрузок и число ошибок
# TODO: вывести ошибки по типам
# TODO: посчитать premium_weight только для express/vip
# TODO: найти клиента-лидера по суммарному весу