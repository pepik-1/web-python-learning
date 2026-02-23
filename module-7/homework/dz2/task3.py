with open('task3given.txt','r',encoding='utf-8') as file:
    lines = []
    for line in file:
        lines.append(line)
    

with open('task3new.txt','w',encoding='utf-8') as file:
    lines = lines[:-1]
    for el in lines:
        file.write(el)