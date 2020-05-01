# Class Variables are shared amongst all instances such as annual raise

class Employee:
    num_of_employess = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.num_of_employess += 1  # we dont need self as its a constant class value

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Mark', 'Banford', 50000)

# lets see the namespace of emp1. We will see there is no raise amount
# since we are inheriting from the parent class

print(emp1.__dict__)

# if we want to give employee 1 5% and not 4%, we can do the following

emp1.raise_amount = 1.10

# now we have added this attribute in the emp1 namespace only
print(emp1.__dict__)
emp1.apply_raise()
print(emp1.pay)

emp2 = Employee('Dan', 'Baker', 50000)
print(emp2.__dict__)
emp2.apply_raise()
print(emp2.pay)


print(Employee.num_of_employess)