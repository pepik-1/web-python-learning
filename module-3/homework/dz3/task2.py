text = str(input('enter a text '))
words = str(input('enter words to upper '))
words_list = words.split(',')
upper_words = []
for el in words_list:
    upper_words.append(el.upper())

for el in upper_words:
    text = text.replace(el.lower(),el)

print(text)