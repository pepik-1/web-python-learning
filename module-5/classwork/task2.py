user = input()
fruits = ['apple','banana','apple','applehmaple','appletytyt']
count_2 = []
for el in fruits:
    if user in el:
        count_2.append(el)
print(len(count_2))