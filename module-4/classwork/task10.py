def func(arr):
    res = []
    for el in arr:
        for i in el:
            res.append(i)
    print(res)

func([[1,2,3],[4,6]])