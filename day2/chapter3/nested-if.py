name1 = 'aminat'
name2 = '67682788'



# if name1.isalpha():
#     if len(name1) > 3:
#         print('its teu')
#     else:
#         print('it is not less grdeater than 3')


# else:
#     print('it is not an alphabet')

username =input('enter your username :')
password = input('enter your password :')

# db_ username = 'aminat'
# db_ password = passygy

# if username !='aminat' :
#     print ('wrong username')
# elif username == 'aminat':
#     print('correct')
# else:
#     print('invalid option')

# if password != 'passygy' :
#     print('wrong password')
# elif password == 'passygy' :
#     print(correct)

db_username = 'aminat'
db_password = 'passygy'


if username !=db_username and password == db_password :
    print('username is wrong')
elif username == db_username and password != db_password :
    print ('password is wrong')
elif username == db_username and password == db_password :
    print ('they are both correct')
elif username != db_username and password != db_password :
    print('both are wrong')
else:
    print('try again')




