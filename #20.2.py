user_data = input(">")
words = user_data.split(' ')

emoji = {
    ":)" :"😂",
    ":(" : "😒"
}

output = ''
for i in words:
    output += emoji.get(i, i) + " "

print(output)