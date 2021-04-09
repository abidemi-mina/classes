def get_even_numbers(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False

even_numbers = list(filter(get_even_numbers,range(10)))
print(even_numbers)

list_numbers = [4,5,7,21,26,30,45,67]
even_numbers2 = list(filter(get_even_numbers,list_numbers))
for e in even_numbers2:
    print(e)


list_numbers = [5,10,15,20,25,30,35,40]
even_numbers3 = list(filter(lambda n : True if (n % 2 == 0) else False,   list_numbers ))
print(even_numbers3)




