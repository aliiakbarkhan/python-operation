name = 'ali akbar khan'
print(name.title())
print(name.upper())
print(name.lower())

firstname = 'ali '
mib_name = 'akbar '
lastname = 'khan'

fullname = firstname + '' + mib_name + '' + lastname
fullname = 'Hi, ' + fullname.lower() + ', how are you'
print(fullname)

striper = 'ali akbar khan    '
print(striper)
print(striper.rstrip())

'''Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?'''

name = 'Eric'
print('Hello ' + name + ', would you like to learn some Python today?')

print('Albert Einstein once said, “A person who never made a\nmistake never tried anything new.”')

'''Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.'''

famous_person = 'ali akbar khan'
message = 'never give up'

print(message)

''': Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().'''

name = '\tali\takbar\tkhan\t'
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
