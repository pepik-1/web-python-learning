import random

nums = [random.randint(-50,50) for _ in range(100)]
best_position = 0
best_sum = None

def min_innterval_pos(i,best_pos=0,best_sum=None):
    if i + 10 > len(nums):
        return best_position
    summ = sum(nums[i:i+10])

    if best_sum == None or summ < best_sum:
        best_sum = summ
        best_pos = i
    return min_innterval_pos(i+1,best_pos,best_sum)
best_pos = min_innterval_pos(0)
print(f'{nums[best_pos:best_pos+10]}')