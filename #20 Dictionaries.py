#we can use dictionary to store key values 

#define
user_data = {
    "name": "Lily",
    "age": "15",
    "email": "Lily_rose.me"
}

#access
print(user_data["age"])

#if you try to access a key that not defined it will give error
#to get around that we can use "get" method 
#and if we try undefined key with get method it will return "None"
print(user_data.get('telephone_number'))

#if that key is not in the dictionary we can also set a value in "get" method
print(user_data.get("birthday", "2005-01-01"))


#we can replace key values
#and we can also add new keys like this
user_data["name"] = "Lily_Rose"
print(user_data["name"])


###    get a number input from user and print it on words