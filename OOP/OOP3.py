# Methods, Class Methods, Static Methods
import datetime


class Employee:
    num_of_employess = 0  # Class Variable
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

    # regular methods in a class take the instance as the first argument (self)
    # How can we change this so it takes the class as the first argument (class method)

    @classmethod  # this ensure we receive our class as the first argument
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod  # creating alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # Tied to the class, since class/instances wont require
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


Employee.set_raise_amt(1.05)  # This deal direct with class method

emp1 = Employee('Jake', 'Smith', 50000)
emp2 = Employee('Janice', 'Dickinson', 60000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# We can use class methods as alternative constructors. This could be due to
# date being passed into the constructor as different. So some employees data
# comes through with in a string separated by '-'


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-40000'
emp_str_3 = 'Jane-Doe-90000'

# usually we would have to split the string

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# but instead of having to parse the string each time, we can create and alt constructor

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.fullname())

# test static method
my_date = datetime.date(2020, 5, 1)
print(Employee.is_workday(my_date))
