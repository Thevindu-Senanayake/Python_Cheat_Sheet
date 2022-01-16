class Person:
    def name(self, name):
        print(f"name: {name}")
    def age(self, age):
        print(f"age: {age}")

Lily = Person()
#its possible to make a object without atribute "name" and "age"
#so that's where the constructor method come in 

#A constructor is a function that gets called at the time of creating an object 

class NewPerson:
    #this is how we define a contructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self, name):
        print(f"name: {name}")
    def get_age(self, age):
        print(f"age: {age}")

Maya = NewPerson("Maya", 18)
Maya.name = "Maya Natalie"
print(Maya.age)