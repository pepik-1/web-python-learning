rows = [
    'INV-100,Keyboard,3,120,paid',
    'INV-101,Mouse,0,40,new',
    'INV-102,Monitor,2,abc,approved',
    'INV-103,Laptop,1,1400,shipped',
    'INV-104,Keyboard,5,110,paid',
    'INV-105,Dock,2,-50,approved',
]


class InvoiceError(Exception):
    pass


class RowFormatError(InvoiceError):
    pass


class QuantityError(InvoiceError):
    pass


class PriceError(InvoiceError):
    pass


class StatusError(InvoiceError):
    pass


def parse_invoice(row):
    id, item ,quantity, price, status = row.split(',')
    try:
        quantity = int(quantity)
    except ValueError:
        raise QuantityError('quantity in not num')
    
    try:
        price = int(price)
    except ValueError:
        raise PriceError('quantity in not num')
    
    try:
        len(row.split(',')) == 5
    except ValueError:
        raise RowFormatError('lack of items in row')
    

    return {'id':id,'item':item,'quantity':quantity,'price':price,'status':status}
     
    
    # TODO: распарсить строку и провалидировать quantity, price, status
    # TODO: при ошибках конвертации использовать raise ... from ...
    


def load_invoices(rows):
    invoices = []
    errors = []
    for el in rows:
        try:
            invoices.append(parse_invoice(el))
        except InvoiceError as e:
            errors.append((el, type(e).__name__,e))

    return (invoices,errors)
    


invoices,errors = load_invoices(rows)
print(invoices,errors)


err = {}
for _,error_type,_ in errors:
    err[error_type] = err.get(error_type,0)+1
print(err)

paid_total = 0

for el in invoices: 
    print(el)
    if el['status'] == 'paid':
        temp = el['price']
        print(temp)
        paid_total += int(temp)
print(paid_total)

max_count = 0
expencive = ''

for el in invoices:
    if el['quantity'] > max_count:
        max_count = (el)['quantity']
        expencive = (el)['item']
print(expencive)

# TODO: вызвать load_invoices(rows)
# TODO: вывести число валидных накладных и число ошибок
# TODO: вывести ошибки по типам
# TODO: посчитать paid_total
# TODO: найти товар-лидер по количеству
