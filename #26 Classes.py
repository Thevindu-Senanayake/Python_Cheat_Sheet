#we can use classes to define new types, to model real concepts
#now let's see how to define a class and work with 'em

#define
class Calculator:
    def add(self):
        print("this method will add values")

    def sub(self):
        print("this method will subtract values")

    def mul(self):
        print("this method will multipy values")

    def divide(self):
        print("this method will divide values")

#makig a object for class
#we can creat objects for one class as many as we want
cal1 = Calculator()
cla2 = Calculator()

#calling to its methods
cal1.add()

#and we also can make atributes
#and this atributes anly belongs to this object we can access it on another object
cal1.x = 10
print(cal1.x)

try:
    print(cal2.x)
except NameError:
    print("this atribute is not defined in this")