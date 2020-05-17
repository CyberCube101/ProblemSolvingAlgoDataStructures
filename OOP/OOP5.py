# Special Methods (dunder)

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):  # This is called before __repr__
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):  # adding employees pay
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Mark', 'Banford', 50000)
emp2 = Employee('Dan', 'Baker', 230000)
print(emp1)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp1.__add__(emp2))
print(len(emp1))
