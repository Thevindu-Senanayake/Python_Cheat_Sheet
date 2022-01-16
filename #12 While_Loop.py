#while is the keyword for while loopes
#while loop takes a condition which means after all it takes a boolean value
#and as long as that condition is true code that we write inside while loop repeatedly executed

# 1
import time
i = 1 
while i <= 5:
    print(i)
    i += 1
    time.sleep(1)
#loop has its own else statement
#this will run if code automatically exit the loop by returning false value from condition   
else:
    print('loop is over')

#2
#as i mentioned before while loop takes boolean value so we can give "True" or "False" as conditions
#if we use True or false as condition it mean that loop will never end
#so we have to end while loop manually we can use "break" keyword for that      
x = 5
while True:
    print(x)
    x -= 1
    time.sleep(x)
    if x == 0:
        break 
#if we manually break down while loop like above this else statement will never trigger
else:
    print("x")    