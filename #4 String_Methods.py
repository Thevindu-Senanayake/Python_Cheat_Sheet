first = "alien's technology"
second = "Lily_Rose"

#"len" function
#this "len" function is general purpose function it means it can have to multiple use cases
print(len(first))

#upper method
print(first.upper())

#lower method
print(second.lower())

#find method
#this find method can be use to find a index of a char
#fint method takes 1 parameter
#if we enter a char that takes more than one places it will out first maching char
# and this method is case sensitive
print(first.find('o'))
#if we pass sequence of char it will out first letter's index
print(second.find("Rose"))

#replace method
#this method takes two parameters that is the text that already there and new text
print(first.replace("technology", "tech"))
print(first)

#if you want to check present of a certain char in a string we use "in" operator
#and this is a expression that provide boolean value it means true or false
#if you print this expression it will give true or false
#the difference between "in" and "find" is find gives a index value and in gives boolean value
print("_" in second)

#split method
#this method will split your string into parts
#this method takes one parameter that is where should the string splits
#and it will return list we will talk about list later
words = second.split("_")
print(words)