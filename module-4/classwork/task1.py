def func(num1,num2):
    count = []
    while num1<num2:
        num1 = num1+1
        if num1%2 == 0:
            count.append(num1)
        else:
            continue
    print(count)

func(2,10)
