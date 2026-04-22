devices_data = [
    ("D-1", "MacBook Pro", "laptop", 45, True),
    ("D-2", "iPad Air", "tablet", 25, True),
    ("D-3", "Canon R50", "camera", 40, True),
    ("D-2", "Duplicate iPad", "tablet", 30, True)
]

rental_ops = [
    ("Алиса", "D-1", 3),
    ("Боб", "D-2", 2),
    ("Кира", "D-2", 4),
    ("Данил", "D-9", 1),
    ("Ева", "D-3", 0)
]


class Device:
    def __init__(self,device_id, title, device_type, daily_price, available):
        self.device_id = device_id
        self.title = title
        self.device_type = device_type
        self._daily_price = daily_price
        self.available = available

    # TODO:
    # реализуй __init__(device_id, title, device_type, daily_price, available)

    @property
    def daily_price(self):
        return self._daily_price

        # TODO:
        # вернуть текущую цену аренды
        

    def set_daily_price(self, value):
        if value > 0:
            self._daily_price = value
            return True
        else:
            return False

        # TODO:
        # если value > 0:
        #    обновить цену и вернуть True
        # иначе вернуть False
        

    def to_dict(self):
        return {'device_id':self.device_id,
                'title':self.title,
                'device_type':self.device_type,
                'daily_price':self._daily_price,
                'available':self.available}

        # TODO:
        # вернуть словарь с полями device_id, title, device_type, daily_price, available
        


class RentalRegistry:
    def __init__(self):
        self.devices = {}
        self.rentals = []
        self.problems = []
        # TODO:
        # self.devices = {}
        # self.rentals = []
        # self.problems = []
        

    def add_device(self, device):
        
        if device.device_id in self.devices:
            self.problems.append((device.device_id, "duplicate device"))
            return
        else:
            self.devices[device.device_id] = device
        





        # TODO:
        # если device.device_id уже есть:
        #    добавить (device.device_id, "duplicate device") в self.problems
        # иначе сохранить устройство
        

    def rent(self, employee, device_id, days):
        if device_id not in self.devices:
            self.problems.append((device_id,'unknown device'))
            return
        
        if days <= 0:
            self.problems.append((device_id,'bad days'))
            return
        device = self.devices[device_id]
        if not device.available:
            self.problems.append((device_id,'not available'))
            return
        total_price = device.daily_price * days
        self.rentals.append({'device_id':device_id,'total_price':total_price})
        device.available = False
        

        # TODO:
        # 1) проверить, что устройство существует
        # 2) проверить, что days > 0
        # 3) проверить, что device.available == True
        # 4) если всё хорошо:
        #    total_price = device.daily_price * days
        #    добавить словарь аренды в self.rentals
        #    device.available = False
        

    def return_device(self, device_id):
        if device_id not in self.devices:
            self.problems.append((device_id,'unknown device'))
            return
        self.devices[device_id].available = True

        # TODO:
        # если device_id нет -> добавить проблему
        # иначе -> self.devices[device_id].available = True
        

    def income_by_type(self):
        income = {}
        for rental in self.rentals:
            device = self.devices[rental['device_id']]
            income.setdefault(device.device_type,0)
            income[device.device_type] += rental['total_price']
        return income



        

        # TODO:
        # вернуть словарь {device_type: total_income}
        pass

    def busy_devices(self):
        busy = []
        for el in devices_data:
            if el[4] == False:
                busy.append(el[4])

        # TODO:
        # вернуть список занятых устройств
        pass

    def build_report(self):
        total_devices = len(devices_data)
        total_rentals = len(self.rentals)
        total_income = 0
        income_by_type = {}
        busy_devices = []
        problems = self.problems
        for rental in self.rentals:
            device = self.devices[rental['device_id']]
            income_by_type.setdefault(device.device_type,0)
            income_by_type[device.device_type] += rental['total_price']
        for device_id , device in self.devices.items():
            if device.available == False:
                busy_devices.append(device.title)
        
        for key,val in income_by_type.items():
            total_income += val



        return {'total_devices':total_devices,
                'total_rentals':total_rentals,
                'total_income':total_income,
                'income_by_type':income_by_type,
                'busy_devices':busy_devices,
                'problems':problems}

        # TODO:
        # вернуть словарь с ключами:
        # total_devices, total_rentals, total_income,
        # income_by_type, busy_devices, problems
        pass


registry = RentalRegistry()

for row in devices_data:
    device = Device(*row)
    registry.add_device(device)

    # TODO:
    # создать Device(*row) и добавить в registry
    

for employee, device_id, days in rental_ops:
    registry.rent(employee, device_id, days)

    # TODO:
    # вызвать registry.rent(employee, device_id, days)
    

report = registry.build_report()

print("Устройств:", report["total_devices"])
print("Успешных аренд:", report["total_rentals"])
print("Доход:", report["total_income"])
print("Доход по типам:", report["income_by_type"])
print("Занятые устройства:", report["busy_devices"])
print("Проблемы:", report["problems"])

