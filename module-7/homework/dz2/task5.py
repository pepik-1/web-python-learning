with open('task5.txt','r',encoding='utf-8') as file:
    search_word = 'Lorem'
    word_count = 0
    for line in file:
        word_count = word_count + line.count(search_word)
print(word_count)