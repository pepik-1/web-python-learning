logs = [
    ('ivan','day',8),
    ('ivan','night',4),
    ('olga','day',6),
    ('petr','night',0),
    ('anna','day',4),
    ('anna','day',3)
        ]

different_days = {}
for el in logs:
    if el[0] not in different_days:
        different_days[el[0]] = set()
    different_days[el[0]].add(el[1])
persons = []
for el in different_days:
    if len(different_days[el]) == 2:
        persons.append(el)
print(persons)
    
person_summ = {}
for el in logs:
    if el[1] not in person_summ:
        person_summ[el[1]] = list()
    person_summ[el[1]].append(el[2])
print(person_summ)

less_eight = []
for el in person_summ:
    if sum(person_summ[el])<8:
        less_eight.append(el)
print(less_eight)