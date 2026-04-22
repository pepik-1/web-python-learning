# file = open('file.txt','r') #1 - what file is(name), 2 - what to do
# print(file.read(1)) 
# print(file.read(1)) 
# file.close #to avoid issues

# r - read
# w - writing with cleaning
# a - append to the end of the file
# x - add a new file
# t - textmode
# b - binmode
# + - read and write
# =================================================
# file = open("C:\windows") - wrong 
# file = open("C:\\windows") - экранирование
# file = open("C:/windows") - best option
#  


# file = open('file.txt', 'w')
# file.write('543')
# file.close()
# # =======
# file = open('file.txt', 'a',encoding="utf-8")
# file.write(' ПЕРСОНА')
# file.close()


# f = open('file.txt','a',encoding="utf-8")
# f.write('1,2,3\n')
# f.write('4,5,6\n')
# f.write('7,8,9')
# f.close

f = open('file.txt','r',encoding='utf-8')
print(f.readline().strip())
print(f.readline().strip())

for line in f:
    print(line.strip())

with open('file.txt','r', encoding="utf-8") as f:
    for line in f:
        print(line.strip())