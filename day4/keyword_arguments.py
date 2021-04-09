def print_kiwadargs(**keys):
    print(keys)


print_kiwadargs(key1='val1',key2='val2',key3='val3')




def state_capital(**states):
    for state , capital in states.items():
        print(f'The capital of {state} is {capital}')


state_capital(imo= 'Owerri', Lagos = 'ikeja', rivers = 'Port Harcourt', niger=' Mina')