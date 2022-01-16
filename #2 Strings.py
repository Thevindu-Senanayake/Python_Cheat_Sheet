#we can use single or double qoutes to define a string variable
first = "alien's technology"
#we can use triple quotes to define multiline string
second = '''Spanish flu, also known as the Great Influenza epidemic or the 1918 influenza pandemic
was an exceptionally deadly global influenza pandemic caused by the H1N1 influenza A virus.
The earliest documented case was March 1918 in Kansas
United States, with further cases recorded in France
Germany and the United Kingdom in April.'''
#we can also use three double quotes to define multiline string
third = """Spanish flu, also known as the Great Influenza epidemic or the 1918 influenza pandemic
was an exceptionally deadly global influenza pandemic caused by the H1N1 influenza A virus.
The earliest documented case was March 1918 in Kansas
United States, with further cases recorded in France
Germany and the United Kingdom in April."""
#print(second)
#we can get specific character from string using this method
print(first[1])
#it takes two args into square first one is starting point and end point
print(first[2:9])
#starting point is normally set to '0' and end point is set to length of string
print(first[:9])
print(first[5:])
#if you use minus(-) values to starting point it take count from end
print(first[-1])
#guess what's output from below line
print(first[1:-1])
