from Lab7 import Pet

class Dog(Pet):
    def self(self, name, age, breed):
        Pet.__init__(self, name, age)
        self.breed=breed
    def intro(self):
        return self.name, self.age, self.breed

name = input("Name: ")
age = input("Age: ")
dog = Pet(name, age)
print(dog.__str__())