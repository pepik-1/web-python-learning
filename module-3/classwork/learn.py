# # text = 'PyThon'
# # print(text[0:7])
# # print(text[::-1])
# # print(text[0:3])

# # print(text.upper())
# # print(text.lower())
# # print(text.capitalize())
# # print(text.swapcase())

# # print(text.find('T'))
# # print(text.index('P'))
# # print(text.replace('P','Z'))
# # print(text.isalpha()) #только буквы
# # print(text.isdigit()) #only nums
# # print(text.isalnum()) #letters and nums
# # print(text.isspace()) #only spaces
# # print(text.isupper()) #only uppers
# # print(text.islower()) #only lowers

# # print(text.strip('n')) #clear right and left parts
# # print(text.lstrip()) #clear left part
# # print(text.rstrip()) #clear right part
# # f = (text.split('T')) #split parts 
# # print(f)
# # print('T'.join(f)) #joins parts



# tupl = (1,2,3)
# tupl2 = tuple([1,2,3])
# tupl3 = 1,2,3
# tuple_1 = tuple(range(0,11))
# print(tuple_1[0])
# print(tupl)
# print(tupl2)
# print(tupl3)

# num1, *other, last_el = tuple(range(0,11))
# print(num1,other,last_el)

# tuple1 = (1,2)
# tuple2 = (3,4)
# print(tuple1 + tuple2)

# pattern = ('a','b')
# repeated = pattern*2
# print(repeated)


# nums = (1,2,3,4,5,6,7,2)
# print(nums.count(2))
# print(nums.index(2))

# num_tuple = tuple(range(0,5))
# for index, num in enumerate(num_tuple):
#     print(index, num)

# ===========================================================================

# user = input('enter str ')
# print(user[::-1])

# =======================================================================
# nums = 0
# letters = 0
# user = input()

# for el in user:
#     if el.isdigit():
#         nums = nums+1

#     if el.isalpha():
#         letters = letters+1

# print(f"цифры:{nums}")
# print(f"буквы{letters}")

# ======================================================================

# user_str = input('enter str ')
# user_symbol = input('enter symbol ')
# print(user_str.count(user_symbol))

# ==========================================================================

# user_str = input('enter words ')
# user_find = input('enter what you need to find ')
# print(user_str.count(user_find))

# ===========================================================================
# beggining = input('enter str')
# find = input('enter what you need to find')
# replace = input('enter with what you need to replace')
# print(beggining.replace(find,replace))


# ==================================================================1

# text = 'pepik loves num 228,loves pipidastr,pipi337.persona.izanagi.arsen.orpheus!'

# splited = text.split('.')
# new = []

# for el in splited:
#     new.append(el.capitalize())

# print(new)


# count = 0
# for el in text:
#     if el.isdigit():
#         count = count+1
# print(count)


# count_znak = 0
# print(text.count(','))

# count_1 = 0
# print(text.count('!'))


# ==================================================================================2

# user_input = input()
# user_count = input()
# print(user_input.count(user_count))

# =================================================================================3

# user = input()
# splited = user.split(' ')
# splited_int = []
# summ = 0
# count = 0
# for el in splited:
#     splited_int.append(int(el))

# for el in splited_int:
#     summ = el + summ
#     count = count + 1

# av = summ/count

# print(summ)
# print(av)


# ===========================================================1

list = [8,6,6,4,-3,2,-4,7]



# negative_summ = 0

# for el in list:
#     if el<0:
#         negative_summ = negative_summ + el
# print(negative_summ)



# even = 0
# for el in list:
#     if el%2 == 0:
#         even = even+el
# print(even)

# noteven = 0
# for el in list:
#     if el%2 == 0:
#         noteven = noteven+el
# print(noteven)


# mult = 1
# for i in range(0, len(list), 3):
#     mult = mult*list[i]
# print(mult)


# product = min(list) * max(list)
# print(product)

# num = 0
# for el in list:
#     if el > 0:
#         num = el
#     else:
#         break

# print(list[0]*num)


# ===================================================================2

list = [8,6,6,4,-3,2,-4,7]


# list2 = []
# for el in list:
#     if el%2 == 0:
#         list2.append(el)
# print(list2)


# list2 = []
# for el in list:
#     if el%2 != 0:
#         list2.append(el)
# print(list2)


# list2 = []
# for el in list:
#     if el<0:
#         list2.append(el)
# print(list2)

summ = 0
for i in range(1,len(list), 1):
    if 