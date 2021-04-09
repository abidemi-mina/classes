#assignment2-1.py
#multilpication table
# m = int(input('enter a number:'))
# X = 1
# while X <= 20 :
#     print(f'{m} x {X} = {m * X}')
#     X+= 1

#assignment2-2.py
# names = ['aminat','sola','abigail','tunde']
# check_name = input('enter a name :')
# if check_name in names:
#     print('name entered is registered')
# else :
#     print('name not in list')

numbers = [10,20,30,40,70,200,300]
total = 0
x = 0
while x < len(numbers):
    total+=  numbers[x]
    x += 1
print('Total', total)
print('Average', total/ len(numbers))
# sum = sum(numbers)
# print(sum)
# average = sum /len(numbers)
# print(average)