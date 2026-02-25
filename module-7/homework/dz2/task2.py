
with open('given.txt','r',encoding = 'utf-8') as file:
    line_count = 0
    for line in file:
        line_count = line_count + 1

with open('given.txt','r',encoding = 'utf-8') as file: 
    length = len(file.read())

with open('given.txt','r',encoding = 'utf-8') as file: 
    glas = ['A','E','I','O','U','Y','a','e','i','o','u','y']
    soglas = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    soglas_res = []
    glas_res = []
    nums = ['1','2','3','4','5','6','7','8','9','0']
    nums_res = []
    for line in file:
        for letter in line:
            if letter in glas:
                glas_res.append(letter)
            if letter in soglas:
                soglas_res.append(letter)
            if letter in nums:
                nums_res.append(letter)

            
# print(soglas_res)
# print(glas_res) 
# print(length)
# print(line_count)
# print(nums_res)

with open('new.txt','w',encoding='utf-8') as file:
    file.write(f'symbvols amount:{length}\n')
    file.write(f'lines amount:{line_count}\n')
    file.write(f'vowel letters:{glas_res}\n')
    file.write(f'consonant letters:{soglas_res}\n')
    file.write(f'numbers amount:{nums_res}\n')
