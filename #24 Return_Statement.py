#if we want to use a value from function to another, we can use return function
#we use "return" keyword to make a return function

def add (val1, val2):
    return val1 + val2  

user_input1 = float(input("enter first value: "))
user_input2 = float(input("enter second value: "))

print(add(user_input1, user_input2))

return_val1 = add(user_input1, user_input2)

def square (val):
    return val * val

print(square(add(user_input1, user_input2)))