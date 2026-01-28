# Пересечение
# set_a = {1,2,3,4}
# set_b = {3,4,5,6}
# result = set_a.intersection(set_b)
# result_operator = set_a & set_b
# set_a &= set_b
# print(set_a, result,result_operator)

# Разность
# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}
# result = set_a.difference(set_b)
# result_operator = set_a - set_b
# set_a -= set_b
# print(set_a, result,result_operator)

# Симметрическая разность
# set_a = {1,2,3,4}
# set_b = {3,4,5,6}
# result = set_a.symmetric_difference(set_b)
# result_op = set_a ^ set_b
# set_a ^= set_b
# print(set_a, result,result_op)

my_set = {1,2,3}
print(3 in my_set)
print(len(my_set))
print(sum(my_set))
print(min(my_set))
print(max(my_set))
for el in my_set:
    print(el)