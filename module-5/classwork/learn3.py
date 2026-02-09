# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2

#     while gap > 0:
#         for i in range(gap,n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j-gap]
#                 j -= gap
#             arr[j] = temp
#         gap //=2
#     return arr

# print(shell_sort([1,6,4,2354,7,4,4,2]))



def quick_sort(arr):
    if len(arr) <= 1:
          return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(sort([1,324,55,65]))