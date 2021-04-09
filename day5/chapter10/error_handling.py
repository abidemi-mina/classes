try:
    import module
    module.print_even(1, 6)
except ModuleNotFoundError as e:
    print(f'{e} this module was not found')

try:
    a = int(input('Enter number1: '))
    b = int(input('Enter number2: '))
    div = a/b
    print(div)
except ZeroDivisionError as z:
    f = open('error.txt', 'a')
    error_message = f'{z} has occured'
    f.write(error_message + '\n')
    print('Something weird happened contact the admin')
