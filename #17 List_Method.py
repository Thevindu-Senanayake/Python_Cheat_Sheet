#so we already talked about String methods so i think its no need to explain about list methods
#so lets take a look at few methods
numbers = [9,2,5,7,9,4.9]
val = [50,654,3258,14,785,1235]

#append
numbers.append(50)
print(numbers)

#insert
#we can use this method to insert items into middle
#and this method takes 2 parameters first one is the index of item that should add your number    
numbers.insert(1,20)
print(numbers)

#remove
#this method directly take the value that we want to remove so we dont need to pass index 
numbers.remove(7)
print(numbers)

#reverse
#this method will rearange order of the items end to start 
numbers.reverse()
print(numbers)

#pop
#with this we can remove last item of a list 
numbers.pop()
print(numbers)

#index
#using this method we can get index of an item
print(numbers.index(2))

#and we also can check the existance of a item
print(50 in numbers)

#count
#this method will give count of value that we pass in 
print(numbers.count(9))

#sort
#this method will sort items in the list in ascending order
numbers.sort()
print(numbers) 

#and we can sort it descending order by using simple trick
print(val)
val.sort()
val.reverse()
print(val)

#copy
#using this method we can simply copy a list 
num2 = numbers.copy()

#clear
#using this method we can clear a entire list
num2.clear()
print(num2)

#so these are the methods that can perform on a list

###    write a programm to remove duplicates of a list