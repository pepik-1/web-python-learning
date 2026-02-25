text1 = []
text2 = []
differ = []
with open('text1.txt','r',encoding = 'utf-8') as file:
     for line in file:
          text1.append(line.strip())

with open('text2.txt','r',encoding = 'utf-8') as file:
     for line in file:
          text2.append(line.strip())

     for i in range(len(text1)):
          if text1[i] != text2[i]:
               differ.append(text1[i])
               differ.append(text2[i])

print(differ)