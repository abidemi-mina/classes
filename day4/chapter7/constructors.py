class Car():
    doors = 3
    windows = 4
    side_mirror = 2

    def __init__(self):
        print('This is a constructor')


    def detail (self,name , color,type):
        return f'The name of the car is {name} and the color is {color} with {self.doors} doors '

car1 = Car()