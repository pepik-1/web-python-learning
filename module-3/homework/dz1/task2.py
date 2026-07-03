text = [9,1,0,3,-5,7,-23,99,0]
negative = 0
positive = 0
zeros = 0
for el in text:
    if el<0:
        negative = negative+1
    if el>0:
        positive = positive +1
    if el == 0:
        zeros = zeros +1
print(max(text))
print(min(text))
print(negative)
print(positive)
print(zeros)