network = {'Me':{'Alice',"Bob"},
           'Alice':{'Me','Chalie','Bob'},
           'Bob':{'Me','David','Eve'},
           'Chalie':{'Alice','Bob'},
           'David':{'Alice','Bob'},
           'Eve':{'Bob'}
           }

user  = 'Me'
friends = network[user]
en_friends = []
result = []
for el in friends:
    en_friends.append(network[el])

for el in en_friends:
    for friend in el:
        if friend not in friends and friend != user:
            result.append(friend)
        else:
            continue
        
print(result)