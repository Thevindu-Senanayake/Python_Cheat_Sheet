#now let's see how to handle some errors and if we get an error let's print a error msg that make scence
#to do it we can use "try and except" block

#this function is not according to rules but i am doing this just to separate this block 
def test ():
    birth_year = int(input("enter your birth year: "))
    current_year = 2018
    age = current_year - birth_year
    print(age)

#that code on top is correct but what if user accidently enter some latters program will crash 
#to avoid it we can use "try and except" function
#if we define a try fuction it also contain except
#we can add except functions more as we want
try:
    birth_year = int(input("enter your birth year: "))
    current_year = 2018
    age = current_year - birth_year
    print(age)
except ValueError:
    print("please enter a numeric value again !")