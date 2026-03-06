rows = [
    ("Алиса", "Python Meetup", "Mon", "registered"),
    ("Алиса", "Python Meetup", "Mon", "attended"),
    ("Боб", "Data Talk", "Tue", "registered"),
    ("Кира", "Data Talk", "Tue", "attended"),
    ("Данил", "Design Review", "Wed", "cancelled"),
    ("Ева", "Python Meetup", "Thu", "waiting"),
    ("Боб", "Data Talk", "Tue", "registered")
]


class AttendanceRecord:
    def __init__(self,person, event_name, day, status):
        self.person = person
        self.event_name = event_name
        self.day = day
        self.status = status
    # TODO:
    # реализуй __init__(person, event_name, day, status)

    def to_dict(self):
        return {
            'person':self.person,
            'event_name':self.event_name,
            'day':self.day,
            'status':self.status
        }

        # TODO:
        # вернуть словарь с полями person, event_name, day, status
        pass

    @classmethod
    def from_tuple(cls, row):
        # TODO:
        # 1) проверить длину row
        if len(row) != 4:
            return None,'Wrong format'
        
        # 2) распаковать значения
        person, event_name, day, status = row

        # 3) проверить статус
        alowed_statuses = {'registred','attended','canceled','waiting'}
        if status not in alowed_statuses:
            return None, 'Wrong status'
        
        # 4) вернуть (record, "") или (None, reason)
        return cls(person, event_name, day, status),''

        


class AttendanceRegistry:
    def __init__(self):
        self.records = []
        self.invalid_rows = []
        self.duplicates = []

        # TODO:
        # self.records = []
        # self.invalid_rows = []
        # self.duplicates = []
        


    def add_record(self, record):
        for existing in self.records:
            if existing.person == record.person and existing.event_name == record.event_name and existing.day == record.day:
                self.duplicates.append((record.person, record.event_name, record.day))
                return
            self.records.append(record)
            
        # TODO:
        # проверить, есть ли уже запись с теми же person, event_name, day
        # если да:
        #    добавить (record.person, record.event_name, record.day) в self.duplicates
        #    не добавлять запись
        # иначе добавить record в self.records
        

    def load_rows(self, rows):
        # TODO:
        # пройти по rows
        # вызвать AttendanceRecord.from_tuple(row)
        # если запись невалидна -> self.invalid_rows.append((row, reason))
        # иначе -> self.add_record(record)
        pass

    def event_stats(self):
        # TODO:
        # вернуть словарь статистики по мероприятиям и статусам
        pass

    def person_history(self, person):
        # TODO:
        # вернуть список записей выбранного участника
        pass

    def active_events(self):
        # TODO:
        # вернуть множество событий, где есть хотя бы один status == 'attended'
        pass

    def build_report(self):
        # TODO:
        # вернуть словарь с ключами:
        # total_valid_records, total_invalid_rows,
        # total_duplicates, event_stats, active_events
        pass


registry = AttendanceRegistry()
registry.load_rows(rows)
report = registry.build_report()

print("Корректных записей:", report["total_valid_records"])
print("Ошибок:", report["total_invalid_rows"])
print("Дублей:", report["total_duplicates"])
print("Статистика мероприятий:", report["event_stats"])
print("Активные мероприятия:", report["active_events"])
