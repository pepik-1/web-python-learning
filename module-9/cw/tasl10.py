from dataclasses import dataclass
from typing import Optional


stocks = {
    'MSK-1': {'keyboard': 10, 'mouse': 20, 'monitor': 4},
    'SPB-2': {'keyboard': 6, 'dock': 5, 'monitor': 2},
    'KZN-3': {'mouse': 7, 'dock': 3, 'laptop': 2},
}

# rows: request_id|client|warehouse_id|sku|quantity
rows = [
    'RQ-100|Acme|MSK-1|keyboard|3',
    'RQ-101|Beta|SPB-2|dock|2',
    'RQ-102|Acme|MSK-1|monitor|5',
    'RQ-103|Delta|X-999|mouse|1',
    'RQ-104|Gamma|KZN-3|laptop|0',
    'RQ-105|Beta|SPB-2|chair|1',
    'RQ-101|Beta|MSK-1|mouse|4',
    'RQ-106|Acme|MSK-1|mouse|7',
    'RQ-107|Kira|KZN-3|laptop|1',
]


class ReservationError(Exception):
    pass


class RowFormatError(ReservationError):
    pass


class WarehouseNotFoundError(ReservationError):
    pass


class ProductNotFoundError(ReservationError):
    pass


class QuantityError(ReservationError):
    pass


class StockLimitError(ReservationError):
    pass


class DuplicateRequestError(ReservationError):
    pass


@dataclass(order=True)
class ReservationRequest:
    request_id: str
    client: str
    warehouse_id: str
    sku: str
    quantity: int


class Warehouse:
    def __init__(self, warehouse_id, products):
        self.warehouse_id = warehouse_id
        self.products = dict(products)
        reservations = []

        # TODO: сохранить warehouse_id
        # TODO: создать отдельную копию словаря products
        # TODO: создать список reservations
        

    def has_sku(self, sku):
        if sku in self.products:
            return True
        return False
        # TODO: вернуть True/False, есть ли такой sku в self.products
        

    def available(self, sku):
        return self.sku
    
        # TODO: вернуть текущий остаток по sku
        

    def reserve(self, request):
        try:
            request.sku
        except:
            raise ProductNotFoundError('Not found')
        
        if request.quantity > self.available:
            raise StockLimitError('wyt')
        
        quantity = quantity - request

        self.reservations.append(request)

        # TODO: если request.sku отсутствует -> raise ProductNotFoundError(...)
        # TODO: если request.quantity > available(...) -> raise StockLimitError(...)
        # TODO: уменьшить остаток на складе
        # TODO: добавить request в self.reservations
        

    def total_left(self):
        return sum(self.products.values)

        # TODO: вернуть сумму всех остатков на складе
        

    def reserved_total(self):
        summ = 0
        for el,val in self.reservations:
            summ += val
        return summ

        # TODO: вернуть сумму quantity по всем self.reservations
        


class ReservationService:
    def __init__(self, stocks):
        self.warehouses = {w_id:Warehouse(w_id,products) for w_id,products in stocks.items()}
        accepted = []
        errors = []
        proccessed_ids = {}
        # TODO: создать warehouses вида warehouse_id -> Warehouse(...)
        # TODO: создать списки accepted и errors
        # TODO: создать множество processed_ids
        

    def parse_request(self, row):
        request_id, client, warehouse_id, sku, quantity_raw = row.split('|')
        quantity_raw = int(quantity_raw)
        try:
            row.split('|') == 5
        except ValueError:
            raise RowFormatError('wrong row items quantity')

        # TODO: split по '|'
        # TODO: ожидать 5 частей: request_id, client, warehouse_id, sku, quantity_raw
        # TODO: quantity_raw преобразовать в int
        # TODO: если warehouse_id не существует -> WarehouseNotFoundError
        try:
            warehouse_id
        except ValueError:
            raise WarehouseNotFoundError('Not exists')

        # TODO: если quantity <= 0 -> QuantityError
        if self.quantity <= 0:
            raise QuantityError('wrong quantity')

        return ReservationRequest(request_id,client,warehouse_id,sku,self.quantity)
        # TODO: вернуть объект ReservationRequest(...)
        

    def submit(self, row):
        try:
            self.parse_request(row)
        
            request = self.parse_request(row)

            if request.request_id in self.processed_ids:
                raise DuplicateRequestError('adwfawfa')
            self.warehouses[request.warehouse_id].reserve(request)
            self.processed_ids.add(request.request_id)
            self.accepted.append(request)
        except RecursionError as e:
            self.errors.append({row,type(e).__name__,str(e)})

            
        # TODO: внутри try вызвать parse_request(row)
        # TODO: если request.request_id уже в processed_ids -> DuplicateRequestError
        # TODO: затем warehouses[request.warehouse_id].reserve(request)
        # TODO: после успеха добавить request_id в processed_ids
        # TODO: добавить request в self.accepted
        # TODO: ReservationError сохранить в self.errors как (row, error_type, message)
        

    def load(self, rows):
        for row in rows:
            self.submit(row)
    
        # TODO: вызвать submit(row) для каждой строки
        

    def client_totals(self):
        totals = {}
        for request in self.accepted:
            totals[request.client] = totals.get(request.client,0)+ request.quantity
        return totals
    
        # TODO: собрать dict вида client -> total_reserved_quantity
        

    def top_client(self):
        totals = self.client_totals()
        return max(totals.items(),key=lambda x: x[1])

        # TODO: использовать client_totals()
        # TODO: вернуть tuple(client, total_quantity) с максимумом
        

    def lowest_stock_warehouse(self):
        warehouse = min(self.warehouses.values(),key=lambda x: x.total_left())
        # TODO: найти склад с минимумом total_left()
        # TODO: вернуть tuple(warehouse_id, total_left)
        return warehouse.warehouse_id, warehouse.total_left()

    def warehouse_snapshot(self):
        return {
            warehouse_id: dict(warehouse.products) for warehouse_id, warehouse in self.warehouses.items()
        }

        # TODO: собрать dict вида warehouse_id -> копия текущих остатков products
        

    def find_request(self, request_id) -> Optional[ReservationRequest]:
        for request in self.accepted:
            if request.request_id == request_id:
                return request
        return None
        # TODO: вернуть Optional[ReservationRequest]
        # TODO: пройтись по self.accepted и найти нужную заявку
        # TODO: если не найдено -> вернуть None
        


service = ReservationService(stocks)

service.load(rows)
print(service.accepted)
print(service.errors)
print(service.warehouse_snapshot())
print(service.client_totals())
print(service.client_totals())
print(service.top_client())
print(service.lowest_stock_warehouse())
print(service.find_request())

# TODO: загрузить rows через service.load(rows)
# TODO: вывести принятые заявки
# TODO: вывести ошибки
# TODO: вывести warehouse_snapshot()
# TODO: вывести client_totals()
# TODO: вывести top_client()
# TODO: вывести lowest_stock_warehouse()
# TODO: вывести find_request('RQ-107')
