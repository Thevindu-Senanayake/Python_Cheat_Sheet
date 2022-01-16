#if a function need a value from user or outside of the function, we can use parameters
#we can use parameters as much as want
#parameter act like local variable that defined in that function
#if we want to call a function with parameter we have to provide a value for that parameter
def welcome_msg(name):
    print(f"hi {name} !")
    print("welcome back")

user_name = input("enter your name: ")
welcome_msg(user_name)

user_name = input("enter your name: ")
welcome_msg(user_name)