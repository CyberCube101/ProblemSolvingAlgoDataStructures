# Inheritance is useful as we can use the Employee class to create more specific class
# like developer class

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


class Manager(Employee):  # A Manager will have a list of employees
    def __init__(self, first, last, pay, employees=None):  # done use mutables as default args
        super().__init__(first, last, pay)  # This lets Employee class handle those args
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


class Developer(Employee):  # This will hold fist, last, pay, Language
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # This lets Employee class handle those args
        self.prog_lang = prog_lang


dev1 = Developer('Mark', 'Banford', 90000, 'Python')
dev2 = Developer('James', 'Smith', 80000, 'Java')

print(dev1.prog_lang, dev1.fullname())
print(dev2.prog_lang, dev2.fullname())

mgr1 = Manager('Sue', 'Smith', 90000, [dev1, dev2])
print(mgr1.print_emps())
mgr1.remove_employee(dev1)
print(mgr1.print_emps())