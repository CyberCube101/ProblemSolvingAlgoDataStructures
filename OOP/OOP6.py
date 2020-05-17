# Getters and Setters and Deleters

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # means can be accessed like an attribute
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')

print(emp1.email)
emp1.first = 'Jim'
print(emp1.fullname)
print(emp1.email)  # still says John Smith even though we change to Jim

# we want to update email automatically when name is changed

emp1.fullname = ('Ted Baker')
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)
