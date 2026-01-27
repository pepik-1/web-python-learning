user_str = input('enter str ')
user_str = user_str.replace(' ','')
user_str = user_str.lower()
reversed_str = user_str[::-1]
if reversed_str == user_str:
    print('Палиндром')
else:
    print('не палиндром')