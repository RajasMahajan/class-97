# file = open("sample.txt", 'a+')

# text = input("enter your lines: ")

# file.write(text)
# file.seek(0)
# print(file.readlines())


file = open('sample.txt', 'a+')
countword = 0 
info = file.readlines()

print(info)

for i in info :
     print(i)
     words = i.split(' ')
     countword = countword+1
     
print(countword)
