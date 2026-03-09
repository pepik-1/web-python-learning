# 1
def devide(a,b):
    return a/b
# print(devide(10,0))

# 2
# raw_values = ['10','5','abc','3']
# numbers = []
# for raw in raw_values:
#     try:
#         numbers.append(int(raw))
#     except ValueError:
#         print(f'{raw} not number ')
# print(numbers)

# 3

# def parse(a,b):
#     try:
#         x = int(a)
#         y = int(b)
#         return x/y
#     except ValueError:
#         return 'a or b is not number'
#     except ZeroDivisionError:
#         return 'you can`t do devision by zero'

# print(parse(10,2))
# print(parse(10,0))
# print(parse('abc','2'))

# # 4

# try:
#     data = {'name':'Alice'}
#     print(data['email'])
# except KeyError as e:
#     print('Тип:',type(e).__name__)
#     print('аргумент:',e.args)
#     print('Сообщение:',e)

# # 5
# def set_discount(persent):
#     if not 0 <= persent <= 100:
#         raise ValueError('discount should be around 1 and 100')
#     return f'discount set: {persent}%'
# print(set_discount(12))
# print(set_discount(1000))

# 6
# def load_user(data,user_id):
#     try:
#         return data[user_id]
#     except KeyError:
#         print(f'user have not found {user_id}')
#         raise
# users = {1:'Alice'}
# try:
#     print(load_user(users,2))
# except KeyError:
#     print('error')

# 7
# class ConfigError(Exception):
#     pass
# def load_port(raw_port):
#     try:
#         return int(raw_port)
#     except ValueError as e:
#         raise ConfigError('PORT must be number') from e

# try:
#     load_port('abc')
# except ConfigError as e:
#     print('Type:' , type(e).__name__)
#     print(type(e).__cause__)

# 8
class EmployeeError(Exception):
    pass
class EmployeeNotFoundError(EmployeeError):
    message_2 = 'employee haven`t found'
    pass
class SalaryValidationError(EmployeeError):
    pass
def find_emoloyee(employees,emp_id):
    if emp_id not in employees:
        raise EmployeeNotFoundError(f'employee {emp_id} haven`t found' )
    return employees[emp_id]
def validate_salary(value):
    if value < 0:
        raise SalaryValidationError('salary can`t be lower than 0')

try:
    find_emoloyee({},10)
except EmployeeNotFoundError as e:
    print(e.message_2)
except SalaryValidationError as e:
    print(e)


# 9
def normalize_persent(x):
    assert isinstance(x,int), 'must be number'
    if not 0 <= x <=100:
        raise ValueError('persent must be around 1 and 100')
    return x / 100

print(normalize_persent(25))
print(normalize_persent('abc'))