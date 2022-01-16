#using nested loops we can do cool thigs like generating x,y condness and so on.

for x in range (3):
    for y in range (3):
        print(f"({x},{y})")

"""
xxxxx
xx
xxxx
xx
xxxxx
"""
#print that "E" shape using nested loops
#for a little tip [5,2,4,2,5] use this to iterate first for loop
#and dont cheat using below code
list = [5,2,4,2,5]
for x_count in list:
    print("x" * x_count)  