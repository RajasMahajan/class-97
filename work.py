
from operator import length_hint


file = open("sample.txt", "a+")
countword = 0 
file.seek(0)
info = file.readlines()

print(info)

for i in info :

     print(i)
     words = i.split(' ')
     countword = countword+len(words)
     
print(countword)