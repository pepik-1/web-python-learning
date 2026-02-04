# def sel(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1,n):
#             if arr[j] <arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx],arr[i]
#     return arr
# print(sel([9,2,4,6,-1,4,5]))



def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])

    return merge(left_part,right_part)

def merge(left_part,right_part):
    i = 0
    j = 0
    result = []
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i+=1
        else:
            result.append(right_part[j])
            j+=1

    result.extend(left_part[i:])
    result.extend(right_part[j:])
    return result

print(merge_sort([9,4,2,-1,6,72,6]))