# 1 . create a class called product
# determine what will be the calss variable for the
# product class and create an init method with three 
# parmeters for the product class, craete another method
# that will calculate the discount prize for each product


class Product():
    discount = 0.20
    def __init__(self,name,amount,image):
        self.n = name
        self.a = amount
        self.i = image
    def method(self):
        payment = self.discount * self.a
        # print(payment)
        return self.a - payment


phone1 =Product('iphone',500000, 'Dope')
print(phone1. method())




# 2. Create a  class called Shirt

class Shirt():

    sleeve  = 'present'
    button = 'present'
    def __init__(self,name):
        self.n = name

class Style(Shirt):
    
    def __init__(self,name,sleeve_len, length):
        super(). __init__(name)
        self.sl = sleeve_len
        self.len = length
    
    def access(self):
            return f'The {self.n} is now accessable'


shirt1 =Style('polo',45,45)
print(shirt1.n)
print(shirt1.access())
print(shirt1.sleeve)
print(shirt1.button)


        # add new parameters that will be a list of sizes in the
# init method of the child class . Create a method that display
# information about this shirt class 
# access the attributes on this child class