
'''
class Person(object):
    pass

def set_name(person, name):
    if len(name) >= 2:
        person.name = name

woman = Person()
set_name(woman, 'Juliana')

print(woman.name)

set_name(woman, "J")

print(woman.name)
'''
'''
class Person(object):
    def set_name(person, name):
        if len(name) >= 2:
            person.name = name
woman = Person()

Person.set_name(woman, "Juliana")

print(woman.name)
'''
'''
class Person(object):
    def set_name(person, name):
        person.name = name

woman = Person()
woman.set_name("Juliana")
print(woman.name)
'''

class Person(object):
    def set_name(self, name):
        if len(name) >= 2:
            self.name = name

woman = Person()
woman.set_name("Juliana")
# print(woman.name)

##############

import string

'''
class CapitalizedPerson(Person):
    def set_name(self, name):
        if name[0] in string.uppercase:
            Person.set_name(self, name)
woman = Person()
woman.set_name("Juliana")
print(woman.name)
'''
