import time

#you learned that we use while loops to execute a block of code multiple times
#in python we have another kind of loop, that is for loop
#and we use that to iterate over items over collection, such as string.

#iterate over string
for x in "Python":
    print(x)

#iterate over list
for name in ['Lily','Maya','Ishitha','Thevindu','Lakshan']:
    print(name)

#iterate over list of numbers
for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num + 5)

#what if we have to iterate over 1000 items.
#on that case we can make a list of 1000 numbers
#or we can use a "range" function
#and range function takes 3 parameters those are starting point ending point and step
#by defualt starting point and step set to 1 and we must enter a ending point
for i in range (1000):
    print(i)
    time.sleep(0.1)