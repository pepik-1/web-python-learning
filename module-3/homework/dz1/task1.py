us = str(input())
res = 0
if us.find('+') == True:
    splited = us.split('+')
    int_list = [int(x) for x in splited]
    res = int_list[0]+int_list[1]
    print(res)

if us.find('-') == True:
    splited = us.split('-')
    int_list = [int(x) for x in splited]
    res = int_list[0]-int_list[1]
    print(res)

if us.find('*') == True:
    splited = us.split('*')
    int_list = [int(x) for x in splited]
    res = int_list[0]*int_list[1]
    print(res)

if us.find('/') == True:
    splited = us.split('/')
    int_list = [int(x) for x in splited]
    res = int_list[0]/int_list[1]
    print(res)

