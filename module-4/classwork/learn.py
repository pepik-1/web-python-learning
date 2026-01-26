def func2():
    for i in range(5):
        yield i

gen = func2()
print(gen)
print(next(gen))

for i in func2():
    print(i)

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print(factorial(9))