#Class name follow camel case
class Dog():
    #pass
    #Class object attribute
    #same for all instance of the object
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    #can pass additional argument
    def bark(self,number):
        print(f'my name is {self.name} and age => {number}....')

my_dog = Dog(breed='Lab',name='Sammy')
print(my_dog.species)
my_dog.bark(10)