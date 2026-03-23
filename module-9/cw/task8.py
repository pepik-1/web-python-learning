from dataclasses import dataclass
from typing import Optional


rooms = {'A-101', 'B-204', 'C-305'}
# rows: booking_id|room_id|owner|start_hour|end_hour
rows = [
    'BK-100|A-101|Alice|9|11',
    'BK-101|A-101|Bob|10|12',
    'BK-102|B-204|Kira|13|15',
    'BK-103|X-999|Oleg|11|12',
    'BK-104|C-305|Eva|16|15',
    'BK-105|B-204|Max|15|17',
]


class BookingError(Exception):
    pass


class RoomNotFoundError(BookingError):
    pass


class TimeRangeError(BookingError):
    pass


class TimeConflictError(BookingError):
    pass


@dataclass(order=True)
class Booking:
    start_hour: int
    end_hour: int
    booking_id: str
    room_id: str
    owner: str


class RoomSchedule:
    def __init__(self, room_id):
        self.room_id = room_id
        self.bookings: list[Booking] = []

        # TODO: сохранить room_id
        # TODO: создать список bookings
        

    def can_add(self, booking: Booking):
        for el in self.bookings:
            if not (booking.end_hour <= el.start_hour or booking.start_hour <= el.end_hour):
                return False
        return True

        # TODO: пройтись по уже существующим booking в self.bookings
        # TODO: проверить пересечение интервалов
        # TODO: если пересечение есть -> вернуть False
        # TODO: если конфликтов нет -> вернуть True
        

    def add_booking(self, booking:Booking):
        if self.can_add(booking) == False:
            raise TimeConflictError('Невозможно создать бронирование из за пересечений')
        self.bookings.append(booking)
        self.bookings.sort(key=lambda b: b.start_hour)
        
        # TODO: если can_add(...) == False -> raise TimeConflictError(...)
        # TODO: добавить booking в self.bookings
        # TODO: отсортировать self.bookings
        

    def total_reserved_hours(self):
        result = 0
        for el in self.bookings:
            result += el.end_hour - el.start_hour
        
        return result

        # TODO: вернуть сумму (end_hour - start_hour) по всем бронированиям комнаты
        


class BookingService:
    def __init__(self, rooms):
        self.shedules = {key:RoomSchedule(key) for key in rooms}
        accepted = []
        errors = []
        



        # TODO: создать schedules вида room_id -> RoomSchedule(room_id)
        # TODO: создать списки accepted и errors
        

    def parse_booking(self, row):
        try:
            booking_id, room_id, owner, start_raw, end_raw = row.split('|')
        except:
            raise 'wrong format'
        
        start_raw = int(start_raw)
        end_raw = int(end_raw)
        if room_id == None:
            raise RoomNotFoundError('Rooms have not found')
        if self.start_hour >= self.end_hour:
            raise TimeRangeError('Time range error')
        
        
        
        return Booking(start_hour=start_raw,end_hour=end_raw,booking_id=booking_id,room_id=room_id,owner=owner) 

        # TODO: split по '|'
        # TODO: ожидать 5 частей: booking_id, room_id, owner, start_raw, end_raw
        # TODO: start_raw и end_raw преобразовать в int
        # TODO: если room_id не существует -> RoomNotFoundError
        # TODO: если start_hour >= end_hour -> TimeRangeError
        # TODO: вернуть объект Booking(...)
        

    def submit(self, row):
        try:
            sucess = self.parse_booking(row)
            self.schedules[self.booking.room_id].add_booking(self.booking)
            self.accepted.append(sucess)
        except:
            self.errors = BookingError(row, error_type, message)
        
        # TODO: внутри try вызвать parse_booking(row)
        # TODO: затем schedules[booking.room_id].add_booking(booking)
        # TODO: успех добавить в self.accepted
        # TODO: BookingError сохранить в self.errors как (row, error_type, message)
        

    def load(self, rows):
        for el in rows:
            el.submit(self.row)

        # TODO: вызвать submit(row) для каждой строки
        

    def busiest_room(self):
        

        # TODO: найти комнату с максимумом total_reserved_hours()
        # TODO: вернуть tuple(room_id, total_hours)
        pass

    def find_booking(self, booking_id):
        # TODO: вернуть Optional[Booking]
        # TODO: пройтись по всем schedules и по всем bookings внутри них
        # TODO: если booking.booking_id совпал -> вернуть booking
        # TODO: если не найдено -> вернуть None
        pass


service = BookingService(rooms)

# TODO: загрузить rows через service.load(rows)
# TODO: вывести принятые бронирования
# TODO: вывести ошибки
# TODO: вывести расписание по всем комнатам
# TODO: вывести busiest_room()
# TODO: вывести find_booking('BK-102')


