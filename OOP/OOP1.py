# Lets say we own a company, we need to keep track
# of employees details

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Mark', 'Banford', 50000)

print(emp1.fullname())  # These are equivalent
print(Employee.fullname(emp1))  # These are equivalent
