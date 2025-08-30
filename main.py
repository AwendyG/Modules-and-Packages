import greetings
# import greetings as g - give it a name to use whn calling it, instead of usong the full name.
# we can import only one function - from greetings import say_hello

name = greetings.say_hello("python")
bye = greetings.say_hello("Tabb")

print(name)
print(bye)

print(greetings.a)
