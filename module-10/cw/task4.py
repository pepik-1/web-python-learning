from dataclasses import dataclass
from typing import Optional


initial_stops = [
    "Склад",
    "ул. Лесная, 10",
    "пр. Мира, 25",
    "наб. Реки, 7",
]

actions = [
    ("append", "ул. Садовая, 3"),
    ("insert_after", "ул. Лесная, 10", "б-р Центральный, 8"),
    ("pop_first", None),
    ("insert_after", "несуществующий адрес", "ул. Тихая, 11"),
    ("append", "ул. Новая, 15"),
]


@dataclass
class StopNode:
    address: str
    next: Optional["StopNode"] = None


class CourierRoute:
    def __init__(self):
        self.head:Optional['StopNode'] = None
        
        # TODO 1: завести поле head
        # TODO 2: в пустом маршруте head должен быть None
        

    def append_stop(self, address: str) -> None:
        new_node = StopNode(address)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current is not None:
            current = current.next
        current = new_node

        # TODO 1: создать новый узел StopNode(address)
        # TODO 2: если head пустой, сделать новый узел головой и завершить метод
        # TODO 3: иначе пройти по списку до последнего узла (у которого next == None)
        # TODO 4: привязать новый узел в конец: last.next = new_node
        

    def insert_after(self, target: str, address: str) -> bool:
        # TODO 1: начать обход с head
        # TODO 2: пока текущий узел существует:
        #   - если current.address == target:
        #       1) создать новый узел
        #       2) новый узел должен ссылаться на current.next
        #       3) current.next перенаправить на новый узел
        #       4) вернуть True
        #   - иначе перейти к следующему узлу
        # TODO 3: если дошли до конца и target не найден, вернуть False
        current = self.head
        while current is not None:
            if current.address == target:
                new_node = StopNode(address)
                current.next = new_node
                return True
            current = current.next
        return False

    def pop_first_stop(self) -> Optional[str]:
        # TODO 1: если head == None, вернуть None
        # TODO 2: сохранить адрес из head.address
        # TODO 3: сдвинуть голову на следующий узел: head = head.next
        # TODO 4: вернуть сохраненный адрес
        if self.head == None:
            return None
        address = self.head.address
        self.head = self.head.next
        return address

    def to_list(self) -> list[str]:
        # TODO 1: создать пустой список result
        # TODO 2: пройтись от head до конца списка
        # TODO 3: на каждом узле добавлять current.address в result
        # TODO 4: вернуть result
        result = []
        current = self.head
        while current is not None:
            result.append(current.address)
            current = current.next
        return result



route = CourierRoute()
for stop in initial_stops:
    route.append_stop(stop)

print("Стартовый маршрут:", route.to_list())

for command, value1, *rest in [(a[0], a[1], None) if a[0] != "insert_after" else (a[0], a[1], a[2]) for a in actions]:
    if command == "append":
        route.append_stop(value1)
        print("append ->", value1)
    elif command == "insert_after":
        target = value1
        new_address = rest[0]
        print("insert_after ->", target, route.insert_after(target, new_address))
    elif command == "pop_first":
        print("pop_first ->", route.pop_first_stop())

print("Финальный маршрут:", route.to_list())
