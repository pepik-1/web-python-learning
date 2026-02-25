with open('task6.txt','r',encoding='utf-8') as file:
    file_data = file.read()

file_r = file_data.replace('Lorem','PEPIK')

with open('task6replaced.txt','w',encoding='utf-8') as file:
    file.write(file_r)