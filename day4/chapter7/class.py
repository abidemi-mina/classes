class Car():
    doors = 3
    windows = 4
    side_mirror = 2

    def detail (self,name , color,type):
        return f'The name of the car is {name} and the color is {color} with {self.doors} doors '


car1 = Car()
print(car1.doors)
print(car1.windows)
print(car1.side_mirror)
print(car1.detail('Toyota','navy','corolla'))


car2 = Car()
print (car2.detail('Toyota','black','sienna'))




