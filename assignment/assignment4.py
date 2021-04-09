# 1 . Create a function thats gives you the sum of numbers in a list . Do not use the python inbuilt funtion
# 2 . Create a funtion that returns the multiplication table of any number passed into it.
# 3 . Use lambda and list comprehension to create a funtion that can add numbers from a lower limit to an upper limit. Call this functionthree times with different values 






# 1
# def sumlist (lists):
#     
#     total = 0
#     for n in lists
#         total+= n
#         
#         return total
        
        



# num = [5,54,97,95,597,9]
#print() sumlist(num)

#list
# def num(digit):
#     x = int(1)
#     while x <= 12:
#         result = digit * x
#         print(f'{digit} x {x} = {result}')
#         x+= 1
        

        
# num(4)




3 
def addition(start,stop):
    add = lambda start,stop : [start for start in range(start,stop)  if start < stop  ]
    cal =sum(add(start,stop))
    return cal
    
# # addition(1,61)
print(addition(32,87))
# print(addition(43,90))
# num(5)








# total = 0
# y = 0
# def addition(x):
#     global total  
#     global y
#     while y < len (x):
#         total += x[y]
#         y+= 1
        #   print(total)
#         return total

# numbers = [ 23,765,234,24]
# print(addition(numbers))

# multiplication

# def multiplication(number):
#     x = int(1)
#     while x <= 12 :
        
#         return number*x
#         x+= 1

# print(multiplication(3))

# CORRECTION
def multiplication(number,start=1, stop=12):
        for start in number 