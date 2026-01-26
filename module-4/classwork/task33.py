def func(n):
    if n <= 0:
        return
    print('*',end=" ")
    func(n-1)

func(5)