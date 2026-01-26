def summ(a,b):
    summm = 0
    if a==b:
        return a
    return a + summ(a+1,b)

print(summ(5,10))