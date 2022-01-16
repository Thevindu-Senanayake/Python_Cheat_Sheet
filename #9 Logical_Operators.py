#logical operators
#there are three logical operators and they are "and" "or" and finally "not"
#you can see the how they works by reading below lines
x = True
y = False
z = True

#and operator
#if we use "and" operation it means we are checking more that one condition 
#to execute that if condition it should true every conditions that checking  
if x and z:
    print("this is a quick demonstration of 'and' operation")
if x and y:
    print('this is not working')

#or operation
#or operation also use to check multiple conditions
#if you use "or" condition it means at least one of checking condition is true python interpreter execute that if condition 
if x or y:
    print("this is a quick demonstration of 'or' operation")

#not operation
#if you use not operation it means if not equal to certain value or not true it will be executed
if not y:
    print("this is a quick demonstration of 'not' operation") 
if x and not y:
    print("so that's it then")
        
class thevindu:
    user_data = input('enter your user name: ')
    password = input('enter your password: ') 

    if user_data == "Lily_Rose" and password == "morning miracle":
        print(f'welcome back agent {user_data}')
    elif user_data == "Lily_Rose" and not password == "morning miracle":
        print("check your user name")
    elif user_data != "Lily_Rose" and password == "morning miracle":
        print("check your password")
    else:
        print("something went to wrong")
