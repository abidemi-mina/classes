class Employee():
    pay_raise = 0.05

    def __init__(self,first_name,last_name,pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p 
        return increment + self.p 
# child class

class Developer(Employee):
     
    def staff_details(self):
      return f'firstname {self.f}, lastname {self.l}'



d1 = Developer('Aminat','Abidemi',9000)
print(d1.f)
print(d1.l)
print(d1.staff_details())
print('Increase in salary by 20% of your salary' ,d1.salary())