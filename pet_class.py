class Pet(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def name(self):
        return self.name
    def age(self):
        return self.age
    def __str__(self):
        return f"My name is {self.name}, {self.age} years old."
    

