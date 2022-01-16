def welcome_msg(first_name, last_name):
    print(f"hi {first_name} {last_name} !")
    print("welcome back")

#as you can see below if you change the position of argument it will give different output
#so we call it "positional Argument"
welcome_msg("Lily", "Rose")
welcome_msg("Rose", "Lily")

#using "keyword arguments" we can assign a argument drectly to a parameter
#so it wont mess with positions
#and if you try to use both types of arguments make sure you use positional arguments first and then keyword args
#otherwise it will het error
welcome_msg(first_name="Maya", last_name="Natalie")

## in most of time we use positional arguments but in certain times we have to use keyword argument
# in most time keyword arguments are use with numericle values
