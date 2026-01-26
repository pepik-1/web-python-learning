def power(a,x):
    if x == 1:
        return a
    return a*power(a,x-1)
print(power(2,5))