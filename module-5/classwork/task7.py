logs = [
    ('ivan','d1','login'),
    ('ivan','d1','view'),
    ('ivan','d2','login'),
    ('olga','d1','login'),
    ('petr','d2','error'),
    ('anna','d1','login'),
    ('anna','d2','view')
]


user_action_count = {}
for user,d,action in logs:
    user_action_count[user] = user_action_count.get(user,0)+1
print(user_action_count)

obj = {}
for user,d,action in logs:
    obj.setdefault(user,list()).append(action)
print(obj)

second_task_us = []
for el in obj:
    if 'error' in obj[el] and 'login' not in obj[el]:
        second_task_us.append(el)
print(second_task_us)

obj_days = {}
for user,d,action in logs:
    obj_days.setdefault(user,list()).append(d)
print(obj_days)

us_more_days = []
for user,days in obj_days.items():
    if len(days) > 1:
        us_more_days.append(user)
print(us_more_days)

first = 0
second = 0
for el in logs:
    if el[1] == 'el1':
        first+=1
    if el[1] == 'el2':
        second+=1
if first>second:
    print('d2')
else:
    print('d1')