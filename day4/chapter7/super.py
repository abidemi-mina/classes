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
    def __init__(self,first_name,last_name,pay,prog_lang):
        super().__init__(first_name,last_name,pay)
        self.prog = prog_lang
        self.email = f'{self.l}.{self.f}@alabiansolutoins.com'
        self.form_email = self.email.lower()
        
    def staff_details(self):
        return f'firstname {self.f}, lastname{self.l}'

d1 = Developer('Aminat','Abidemi',9000,'Python')
print(d1.prog)
print(d1.form_email)
print(d1.staff_details())
print(d1.email)