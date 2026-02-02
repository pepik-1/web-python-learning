nums = [1,2,993,4,25,5,335,8,8,9,-99,0]
result = {}
for el in nums:
    n = len(str(abs(el)))
    result[n] = result.setdefault(n,0)+1
for el in sorted(result):
    print(f"{el}:{result[el]}")
    