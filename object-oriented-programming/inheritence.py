class Animal():
    def __init__(self):
        print('Animal created')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('''I am eating
              ...love to eat
              ...going for vacation.....''')
"""
animal = Animal()
animal.eat()
"""
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    #method override
    def who_am_i(self):
        print('I am dog.....')

        
mydog = Dog()
mydog.who_am_i()