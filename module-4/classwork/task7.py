def func(num):
    splited = list(map(int, str(num)))
    num_1 = splited[0]+splited[1]+splited[2]
    num_2 = splited[3]+splited[4]+splited[5]
    if num_1 == num_2:
        return 'lucky!!!'
    else: 
        return 'bad luck!!!'

print(func(123420))