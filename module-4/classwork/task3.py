def func(len,direct,symb):
    line = ''
    if direct == 'vertical':
        for i in range(0,len,1):
            print(symb)
            
    elif direct == 'horizontal':
        line = symb * len
    print(line)
func(8,'vertical','*')