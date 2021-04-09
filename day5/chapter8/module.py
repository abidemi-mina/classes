class Employee():
    pay_raise = 0.20

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p
        return increment + self.p


def print_even(start, stop):
    '''
        The start and stop parameter are required
        start takes an integer as a value and 
        stop takes an integer as a value
        returns several integers
    '''
    while start <= stop:
        if start % 2 == 0:
            print(start)
        start += 1
