delivery_orders = [
    {"order_id": "ORD-901", "carrier_code": "fast", "city": "Moscow", "address": "Lenina 10", "weight_kg": 1.2},
    {"order_id": "ORD-902", "carrier_code": "box", "city": "Kazan", "address": "Pushkina 5", "weight_kg": 3.4},
    {"order_id": "ORD-903", "carrier_code": "city", "city": "Sochi", "address": "Primorskaya 8", "weight_kg": 0.8},
    {"order_id": "ORD-904", "carrier_code": "fast", "city": "Perm", "address": "Mira 21", "weight_kg": 5.0},
    {"order_id": "ORD-905", "carrier_code": "unknown", "city": "Tula", "address": "Sadovaya 3", "weight_kg": 2.1},
]

carrier_mapping = {
    "fast": "FastShip",
    "box": "BoxBerry",
    "city": "CityExpress",
}

#  destination: str, weight: float
class FastShipAPI:
    def create_order(self, order_id: str):
        # TODO 1: верните словарь в формате FastShip:
          return{
              'provider': 'FastShip',
              'id': order_id,
              'track': f'FS-{order_id}',
              'state': 'created'
          }
        


class BoxBerryGateway:
    def register_delivery(self, payload: dict):
        # TODO 2: верните словарь в формате BoxBerry:
        #   {
        #       'service_name': 'BoxBerry',
        #       'order_ref': payload['order_ref'],
        #       'tracking_code': f"BB-{payload['order_ref']}",
        #       'result': 'accepted'
        #   }

        return  {
              'service_name': 'BoxBerry',
              'order_ref': payload['order_ref'],
              'tracking_code': f"BB-{payload['order_ref']}",
              'result': 'accepted'
          }
        


class CityExpressService:
    def push_task(self, *, external_id: str, city: str, address: str, mass: float):
        # TODO 3: верните словарь в формате CityExpress:
        #   {
        #       'carrier_title': 'CityExpress',
        #       'external_id': external_id,
        #       'awb': f'CE-{external_id}',
        #       'delivery_status': 'queued'
        #   }
        return   {
              'carrier_title': 'CityExpress',
              'external_id': external_id,
              'awb': f'CE-{external_id}',
              'delivery_status': 'queued'
          }
        
        


class FastShipAdapter:
    def __init__(self, api):
        # TODO 4: сохраните api
        self.api = api

    def ship(self, order: dict) -> dict:
        # TODO 5: вызовите FastShipAPI.create_order(...)
        new_order = self.api.create_order(order)
        # TODO 6: преобразуйте ответ в единый формат:
        #   carrier, order_id, tracking_number, status
        return {'carrier':new_order['provider'],'order_id':new_order['id'],'tracking_number':new_order['track'],'status':new_order['state'] }


class BoxBerryAdapter:
    def __init__(self, gateway):
        # TODO 7: сохраните gateway
        self.gateway = gateway

    def ship(self, order: dict) -> dict:
        # TODO 8: соберите payload для BoxBerryGateway.register_delivery(...)
        #   payload должен содержать: order_ref, destination, weight_kg
        new_payload = self.gateway.register_delivery({
            'order_ref': order['order_id'],
            'destination': f'{order["city"]},{order['address']}',
            'weight_kg':order['weight_kg']
            
        })
        print(new_payload)
        return {'order_ref':new_payload['order_ref'],'destination':new_payload['destination'],'weight_kg':new_payload['weight_kg']}
        
        # TODO 9: преобразуйте ответ в единый формат
        


class CityExpressAdapter:
    def __init__(self, service):
        # TODO 10: сохраните service
        self.service = service

    def ship(self, order: dict) -> dict:
        # TODO 11: вызовите CityExpressService.push_task(...)
        new_city = CityExpressService.push_task(order)
        # {
        #       'carrier_title': 'CityExpress',
        #       'external_id': external_id,
        #       'awb': f'CE-{external_id}',
        #       'delivery_status': 'queued'
        #   }
        # TODO 12: преобразуйте ответ в единый формат
        return {'carrier_title':new_city['carrier_title'],'external_id':new_city['external_id'],'awb':new_city['awb'],'delivery_status':new_city['delivery_status']}


adapters = {
    "fast": FastShipAdapter(FastShipAPI()),
    "box": BoxBerryAdapter(BoxBerryGateway()),
    "city": CityExpressAdapter(CityExpressService()),
}

shipment_results = []
carrier_stats = {}
successful_tracking_numbers = []
failed_orders = []

for order in delivery_orders:
    adapter = adapters.get(order["carrier_code"])

    
    # TODO 13: если адаптер не найден:
    #   - добавьте order['order_id'] в failed_orders
    #   - перейдите к следующему заказу
    if adapter is None:
        failed_orders.append(order['order_id'])
        continue

    
    result = adapter.ship(order)
    shipment_results.append(result)
    # TODO 14: вызовите adapter.ship(order) и сохраните result
    # TODO 15: добавьте result в shipment_results

    # TODO 16: увеличьте счетчик carrier_stats[result['carrier']]
    print('---',order["carrier_code"])
    carrier_stats[result['carrier']] = carrier_stats.get(result['carrier'],0) + 1

    # TODO 17: если result['status'] находится в ['created', 'accepted', 'queued']:
    #   добавьте result['tracking_number'] в successful_tracking_numbers
    if result['status'] in ['created', 'accepted', 'queued']:
        successful_tracking_numbers.append(result['tracking_number'])


print('Результаты отправки:')
print(shipment_results)
print()

print('Количество отправок по перевозчикам:')
print(carrier_stats)
print()

print('Успешные трек-номера:')
print(successful_tracking_numbers)
print()

print('Заказы с ошибкой выбора перевозчика:')
print(failed_orders)
