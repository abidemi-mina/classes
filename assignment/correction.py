# 1. Using any of the conditional statement learnt to write a simple Python program that will output the score and remark eg “Your score is 76 and this is Excellence” using the algorithm below. Make sure that invalid score such value greater than 100 or less than 1 are detected and reported
#  0 – 34 = Fail
#  35 – 44 = Pass
#  45 – 49 = Fair
#  50 – 59 = Good
#  60 – 69 = Very Good
#  70 – 100 = Excellence

# score = 5

# if score >= 0 and score < 35:
#     grade = 'Fail'
#     print(f'Your score is {score} and your grade is {grade}')
# elif score >= 35 and score < 45:
#     grade = 'Pass'
#     print(f'Your score is {score} and your grade is {grade}')
# elif score >= 45 and score < 50:
#     grade = 'Fair'
#     print(f'Your score is {score} and your grade is {grade}')
# elif score >=50 and score < 60:
#     grade = 'Good'
#     print(f'Your score is {score} and your grade is {grade}')
# elif score >= 60 and score < 70:
#     grade = 'Very Good'
#     print(f'Your score is {score} and your grade is {grade}')
# elif score >= 70 and score <= 100:
#     grade = 'Excellence'
#     print(f'Your score is {score} and your grade is {grade}')
# else:
#     print(f'Your score is invalid')

# 2. Write a program in python that will print the lowest number among three numbers supplied

# num1 = 5
# num2 = 10
# num3 = 20

# if num1 < num2 and num1 < num3:
#     print(f'{num1} is less than {num2}  and {num3}')
# elif num2 < num1 and num2 < num3:
#     print(f'{num2} is less than {num1}  and {num3}')
# elif num3 < num1 and num3 < num2:
#     print(f'{num3} is less than {num1}  and {num2}')

# 1. Create a multiplication table program using while loop, this will be done in such a way that when a user supplies any number 
# the multiplication table of that number will be created.

# num = 4
# x = 1
# while x <= 12:
#     result = num * x
#     print(f'{num} X {x} = {result}')
#     x += 1

# Write a program that sums all the numbers in a 
# list 10, 20, 30, 40, 70, 200, 300 and also determine the average.

numbers = [10, 20, 30, 40, 70, 200, 300]
print(numbers[0])

total = 0
x = 0

# while 0 < len(numbers):
#     total += numbers[0]
#     # 10
#     0 = 0 + 1

# while 1 < len(numbers):
#     total += numbers[1]
#     # 30
#     2 = 1 + 1
# while 2 < len(numbers):
#     total += numbers[2]
#     # 60
#     3 = 1 + 2

# while x < len(numbers):
#     total += numbers[x]
#     x += 1
# print('Total ', total)
# print('Average ', total/len(numbers))

# Write a program that returns even numbers from 1 to 20
# using while loop


# x = 1
# while x <= 20:
#     if x % 2 == 0:
#         print(x)
#     x += 1



# Create a python list with email and password
# display an error message if email is not in the
# list, if the email is in the list check if the
# two password fields matches, and if it does, change the
# password to a new one and dispplay success message

data = ['ben@yahoo.com', 'pass12345']
email = 'ben10@yahoo.com'
password = 'pass123456'
confirm_password = 'pass1234567'


# if email != data[0]:
#     print('Email does not exist')
# elif password != confirm_password:
#     print('Password do not match')
# elif password == confirm_password:
#     data[1] = password
#     print('Password changed successfully')
# print(data)


if email != data[0]:
    print('Email does not exist')
elif email == data[0]:
    if password == confirm_password:
        data[1] = password
        print('Password changed successfully')
        print(data)
    else:
        print('Password do not match')
    









