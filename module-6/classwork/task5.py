history = [
    ('t_1', 'new'),('t_1','in_progress'),("t_1",'done'),
    ('t_2' ,"new"),('t_2',"done"),
    ('t_3','new'),('t_3','in_progress'),('t_3','canceled'),
    ('t_4','new'),('t_4','canceled'),('t_4','done'),
]
allowed = {('new','in_progress'),('in_progress','done'),('new','canceled'),('in_progress','canceled')}
ids = {}
for el in history:
    if el[0] not in ids:
        ids[el[0]] = []
    if el[0] in ids:
        ids[el[0]].append(el[1])
print(ids)



# for el in history:
#     if el[0] not in temp:
#         temp[el[0]] = []
#     if el[0] in temp:
#         temp[el[0]].append(el[1])

# print(temp)

# for el in temp:
#     if temp[el][1] == 'canceled':
#         continue

#     elif temp[el][0] != 'new':
#         print(f'{el} - wrong')
    
#     elif temp[el][1] == 'done':
#         print(f'{el} - wrong')
#         continue

#     elif temp[el][1] != 'in_progress':
#         print(f'{el} - wrong')
        
#     elif temp[el][2] != 'canceled' or 'done':
#         print(f'{el} - wrong')
    
#     print(temp[el][2])
    
        


