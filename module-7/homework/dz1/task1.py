id_ = [4,1,3,2]
num = [55,34,77,8]

def pr_info():
    for i, n in enumerate(id_):
        print(f'id : {n},  номер : {num[i]}')
    print('----------------------')
    
def sort_(sample, convert):
    n = len(sample)
    for i in range(n-1):
        for j in range(n-i-1):
            if sample[j] > sample[j+1]:
                sample[j], sample[j+1] = sample[j+1], sample[j]
                convert[j], convert[j+1] = convert[j+1], convert[j]
    

print('справочник')
pr_info()
sort_(id_, num)
print('справочник отсортирован по идентификационным кодам')
pr_info()
sort_(num, id_)
print('справочник отсортирован по номерам телефона')
pr_info()














