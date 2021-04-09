# numbers = []

# for n in range(1,12):
#     numbers.append(n)
# print (numbers)

# even = []
# for n in range(1,12):
#     if n % 2 ==0:
#         even.append(n)
# print (even)


# #USING LIST COMPREJENSION
# numbers = [n for n in range(1,12)]
# print(numbers)

# even = [n for n in range(1,12) if n %2 == 0]
# print(even)

lamda_even = lambda start,stop :[start for start in range(start,stop) if start %2 == 0]
print(lamda_even(1,12))