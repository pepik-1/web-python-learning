stocks = {
    "keyboard": 10,
    "mouse": 8,
    "monitor": 4,
}

commands = [
    "remove|keyboard|2",
    "add|mouse|3",
    "report",
    "remove|monitor|5",
    "undo",
    "remove|keyboard|4",
    "report",
    "undo",
    "undo",
    "undo",
    "report",
]

history_stack = []
snapshots = []
errors = []
undo_count = 0

for command in commands:
    if command == "undo":
        # TODO 1: проверить, есть ли что откатывать (history_stack не пуст)
        # TODO 2: если есть, взять последнее состояние через pop()
        # TODO 3: присвоить stocks это состояние
        # TODO 4: увеличить undo_count на 1
        # TODO 5: если стек пуст, просто ничего не делать
        
        if history_stack:
            stocks = history_stack.pop()
            undo_count += 1
        

        continue

    if command == "report":
        # TODO 1: сделать копию текущего словаря stocks
        # TODO 2: добавить копию в snapshots
        
        copy_stocks = stocks.copy()
        snapshots.append(copy_stocks)

        continue

    action, sku, qty_raw = command.split("|")
    qty = int(qty_raw)

    if action == "add":
        # TODO 1: перед изменением положить копию stocks в history_stack
        # TODO 2: увеличить остаток sku на qty
        #   подсказка: для универсальности можно использовать stocks.get(sku, 0)
        history_stack.append(stocks)
        stocks.get(sku, 0) + qty

    elif action == "remove":
        # TODO 1: взять текущий остаток товара (например, через stocks.get(sku, 0))
        # TODO 2: если текущий остаток < qty:
        #   - НЕ менять склад
        #   - добавить текст ошибки в errors
        # TODO 3: иначе (товара хватает):
        #   - сохранить копию stocks в history_stack
        #   - уменьшить остаток по sku на qty

        remain = stocks.get(sku, 0)
        if remain < qty:
            errors.append(f'Остаток меньше {sku}')
        else:
            history_stack.append(stocks.copy())
            remain -= qty
        


print("Снимки склада:", snapshots)
print("Ошибки:", errors)
print("Успешных undo:", undo_count)
print("Финальные остатки:", stocks)
