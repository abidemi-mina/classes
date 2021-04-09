# south_east = ['Imo','Abia','AnEbonyiabmra','Enugustate','Oyo']
# for state in south_east:
#     print(state)

# 'break'

# num1 = int(input('enter a number :'))
# for x in range(1,13):
#     print(f'{num1} x {x} = {num1 * x}') 


states = {
    'lagos' : 'Ikeja',
    'Ondo' : 'Akure',
    'Oyo' : 'Ibadan',
    'Bayelsa' : 'Yenogoa'
}
for s in states:
    print(states[s])

print('BREAK')

#for 
for s in states.values():
    print(s)

print('BREAK')

# for keys 
for s in states.keys():
    print(s)

print('BREAK')

#for items
for s,y in states.items():
    print(s,y)

