text1 = [9,1,0,3,-5,7,-23,99,0]
text2 = [7,3,6,1,0,-99,29,-1,7,7,7,7,7]

text_both = text1+text2

text_no_repeats = []

text_same =[]

text_unique = []

text_min_max = []

for el in text_both:
    if el in text_no_repeats:
        continue
    else:
        text_no_repeats.append(el)

for el in text2:
    if el in text1:
        text_same.append(el)


for el in text2:
    if el not in text1:
        text_unique.append(el)

text_min_max.append(min(text1))
text_min_max.append(min(text2))
text_min_max.append(max(text2))
text_min_max.append(max(text1))
