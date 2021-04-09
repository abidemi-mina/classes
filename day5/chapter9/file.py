file = open('content.txt', 'r')
print(file.read())

for f in file:
    print(f)

e = open('error.txt', 'a')
writeup = input('Put stuff here: ')
e.write(writeup + '\n' )