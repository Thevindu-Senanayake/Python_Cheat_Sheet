frist_name = "lily"
last_name = "rose"
age = 14
new_msg = (frist_name + "(" + last_name + ")" + "is a programmer")
print(new_msg)

#if you want to do something like in line 3 there is a short method to do it and its called formatted string
msg = f'{frist_name} [{last_name}] is a programmer and {age} years old'
print(msg)

#to define a formatted string all you have to do is put "f" before quotes
#and you can use curly brackets to input other varibles