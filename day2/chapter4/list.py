# person = ['Aminat', 43, True , 'Dark']
# print(f'My name is {person[0]}, I am {person[1]}years old and I am  {person[3]} in complexion')

# # adding an item to a list at the end
# person.append('rael')
# # changing value of an item
# person[1] = 23
# # addingb at a spcific place
# person.insert(1,'dark hair')

# print(person) 


detail_db = ['aminat','aminat121','abidemi212']
password = input('enter password :')
password2 = input('enter password2 :')
if len(password )< 7:
    print('it is above the limit')
elif password != password2:
    print('both password do not match')
else:
    password = detail_db[1]
    print('password changed successfully')
    # print('both password have being changed')

