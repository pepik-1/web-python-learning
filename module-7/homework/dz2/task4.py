with open('task4.txt','r',encoding='utf-8') as file:
    longest = 0
    for line in file:
        line = len(line)
        if line > longest:
            longest = line
print(longest)