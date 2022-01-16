value = [1,2,3,4,5,6,7,8,9]
print(value.append(50))

#that code block in below if you run it it will print "None"
#so "None" is a object in python that represents absence of a value
#that is because that method is not returning any value 
#so instead of printing return value of that method, simply call it to do that function 
#then print the list after it 
value.insert(3, 70)
print(value)