message = 'Hello world' #make variable names all lowercase, use underscores as spaces in words

message_1 = "Andrew's World"

message_2 = """Andrew's
World extended onto multiple lines"""

print(message_2)
print(message_1)
print(message)

# if you want to print the character length of the message

print(len(message_2))

# and we can access each character seperately using square brackets

print(message[0])
print(message[0:5])

print(message.lower())
print(message.upper())

# count the l's

print(message.count('l'))

#repalcing words in a string with a different word
new_message = message.replace("world", 'Universe')
print(new_message)

#concatenated strings besides plus sign

name = "Andrew"
name2= "Micheal"
greeting = "Hello"

message = "{} {} and {}".format(greeting, name, name2)
print(message)

