class Employee():
    pay_raise = 0.05

    def __init__(self,first_name,last_name,pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p 
        return increment + self.p 


el1 = Employee('Benedict','Uwazie', 2000)
el1.f = 'Chukwuemeka'
print(el1.f,el1.l)
print(el1.salary())


e2 = Employee('Alabi','Adebayo', 7000)
print(e2.f)
print(e2.salary())