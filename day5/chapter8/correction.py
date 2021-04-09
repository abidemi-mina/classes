#1 Create a Class called Product
#   determine what will be the class varible for the
# the product class and create an init method with three
# parameters for the product class, create another method
# that will calculate the discount prize for the each product
# call three times

class Product():
    percent_discount = 0.10

    def __init__(self, name, actual_prize, image):
        self.n = name
        self.a = actual_prize
        self.i = image

    def discount_method(self):
        discount = self.percent_discount * self.a
        return self.a - discount


p1 = Product('LG', 5000, 'lg.jpg')
print(p1.n)
print(p1.a)
print(p1.discount_method())

#2  Create a child class called Shirt
#  add new paramter that will be a list of sizes in the
#  init method of the child class. Create a demethod that
# display information about this shirt class.
# access the attributes on this child class

class Shirt(Product):
    def __init__(self, name, actual_prize, image, sizes):
        super().__init__(name, actual_prize, image)
        self.s = sizes

    def display_info(self):
        print('Product name: ', self.n)
        print('Product actual prize: ', self.a)
        print('Product image: ', self.i)


s1 = Shirt('Trouser', 6500, 'trouser.jpg', ['LG', 'XL', 'SM'])


s1.discount_method()

print('Print sizes below')
for s in s1.s:
    print(s)
print('Printing second item')
print(s1.s[1])



