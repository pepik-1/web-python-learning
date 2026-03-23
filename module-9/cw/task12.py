# rows: pass_id|member_name|plan|days_left|status
rows = [
    'PS-100|Alice|flex|12|active',
    'PS-101|Bob|fixed|20|paused',
    'PS-102|Team Rocket|team|0|expired',
    'PS-103|Diana|flex|6|active',
]


class CoworkingPass:
    allowed_plans = {'flex', 'fixed', 'team'}
    allowed_statuses = {'active', 'paused', 'expired'}

    def __init__(self, pass_id, member_name, plan, days_left, status):
        try:
            plan = int(plan)
            status != 'expired'
        except ValueError:
            raise ValueError('not int')
        if plan < 0 or status != 'expired' :
            raise ValueError('plan < 0 or status != expired')
        
        self.pass_id = pass_id
        self.member_name = member_name
        self.plan = plan
        self.status = status
        self._days_left = days_left
        
    # def days(self,value):
    #     if value <0:
    #         raise ValueError('days must be > 0')
    #     self._days_left = value
    #     return value
        
            
        # TODO: проверить plan и status, иначе raise ValueError(...)
        # TODO: сохранить pass_id, member_name, plan, status
        # TODO: days_left хранить через внутреннее поле self._days_left
        # TODO: значение days_left пропустить через property/setter
        

    @property
    def days_left(self):
        return self._days_left
        # TODO: вернуть текущее число оставшихся дней
        

    @days_left.setter
    def days_left(self, value):
        value = int(value)
        if value < 0:
            raise ValueError('Days must be >= 0')
        value = self._days_left
        return value
        # TODO: привести value к int
        # TODO: если value < 0 -> raise ValueError('Days must be >= 0')
        # TODO: сохранить результат в self._days_left
        

    def use_day(self):
        if self.status != 'active':
            raise ValueError('Not active')
        if self.days_left == 0:
            raise ValueError('days must be >0')
        self.days_left -= 1
        if self.days_left == 0:
            self.status = 'expired'

        # TODO: если статус не 'active' -> raise ValueError(...)
        # TODO: если days_left == 0 -> raise ValueError(...)
        # TODO: уменьшить days_left на 1
        # TODO: если после списания days_left == 0, перевести статус в 'expired'
        

    def pause(self):
        if self.status == 'expired':
            raise ValueError('expired')
        self.status = 'paused'
        # TODO: если статус 'expired' -> raise ValueError(...)
        # TODO: перевести пропуск в 'paused'
        

    def resume(self):
        if self.days_left == 0:
            raise ValueError('days_left == 0')
        self.status = 'active'
        # TODO: если days_left == 0 -> raise ValueError(...)
        # TODO: перевести пропуск в 'active'
        

    def renew(self, extra_days):
        extra_days = int(extra_days)
        if extra_days <= 0:
            raise ValueError('no extra days')
        self.days_left += extra_days
        if self.days_left > 0 and self.status == 'expired':
            self.status = 'active'

        # TODO: привести extra_days к int
        # TODO: если extra_days <= 0 -> raise ValueError(...)
        # TODO: увеличить days_left
        # TODO: если days_left > 0 и статус был 'expired', перевести в 'active'
        

    @classmethod
    def from_row(cls, row):
        pass_id, member_name, plan, days_left, status = row.split('|')
        return CoworkingPass(pass_id, member_name, plan, days_left, status)

        # TODO: split по '|'
        # TODO: ожидать 5 частей: pass_id, member_name, plan, days_left, status
        # TODO: вернуть CoworkingPass(...)
        

    def __repr__(self):
        return CoworkingPass(pass_id='pass_id', member_name='member_name', status='status', days_left='days_left')
        # TODO: вернуть строку вида CoworkingPass(pass_id='...', member_name='...', status='...', days_left=...)
        


class CoworkingRegistry:
    def __init__(self):
        self.items = []

    def add(self, coworking_pass):
        self.items.append(coworking_pass)

        # TODO: добавить объект в self.items
        

    def load(self, rows):
        for row in rows:
            result = CoworkingPass.from_row(row)
            self.add(result)

        
        # TODO: для каждой строки создать CoworkingPass.from_row(row)
        # TODO: добавить объект в реестр через add(...)
        

    def active_passes(self):
        actives = []
        for el in self.items:
            if el[self.status] == 'active':
                actives.append(el[self.status])
        return actives
        # TODO: вернуть список пропусков со статусом 'active'
        

    def by_plan(self, plan):
        plan_list = []
        for el in self.items:
            if el[self.plan] == plan:
                plan_list.append(el[self.plan])
        # TODO: вернуть список пропусков нужного тарифа
        
        

    def total_days_left(self):
        summ = 0
        for el in self.items:
            summ += el[self.days_left]
        
        # TODO: вернуть суммарное число оставшихся дней
        

    def status_summary(self):
        dict_status = {}
        for el in self.items:
            dict_status.setdefault(el[self.status],0) + el[self.days_left]

        return dict_status()
    
        # TODO: собрать dict вида status -> count
        

    def find(self, pass_id):
        status = None
        for el in self.items:
            if el[self.pass_id] == pass_id:
                status = el[self.status]
        return status
            

        # TODO: вернуть пропуск по pass_id или None
        

    def largest_balance(self):
        days_l = {}
        for el in self.items:
            days_l.setdefault(el[self.status],0) + el[self.days_left]
        
        max_cp = max(self.items,key=lambda x:x.days_left)

        # TODO: найти пропуск с максимальным days_left
        # TODO: вернуть tuple(pass_id, days_left)
        return max_cp.pass_id,max_cp.days_left


registry = CoworkingRegistry()

for row in rows:
    registry.add(row)

print(registry.status_summary())

# TODO: загрузить rows в registry
# TODO: вывести все пропуска
# TODO: вывести active_passes()
# TODO: вывести by_plan('flex')
# TODO: вывести total_days_left()
# TODO: вывести status_summary()
# TODO: найти пропуск 'PS-101', возобновить его и вывести status_summary()
# TODO: найти пропуск 'PS-100', списать один день и вывести объект
# TODO: найти пропуск 'PS-102', продлить на 5 дней и вывести объект
# TODO: вывести largest_balance()
        
