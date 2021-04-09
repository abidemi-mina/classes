def double_numbers(n):
    n += n
    return n


double = list(map(double_numbers, range(9)))
print(double)


def expo_numbers(n):
    n **= 3
    return n

exponetia = list(map(expo_numbers, range(6)))
print(exponetia)

exop2 = list(map(lambda n : n**3, range(6)))
print(exop2)
exop3 = list(map(lambda n : n**n, range(6)))
print(exop3)
exop4 = list(map(lambda n : n**7, range(6)))
print(exop4)
minus = list(map(lambda n : n-2, range(7)))
print(minus)
divd = list(map(lambda n : n/2, range(7)))
print(divd)
mut = list(map(lambda n : n*4, range(7)))
print(mut)