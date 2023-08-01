def greet():
    print("HI")
    print("My name is Ateeth")
    print("Hope u are doing well")


greet()


# Function that allows for input
def greet_with_name(name):
    print(f"Hi {name}")
    print("I am Ateeth Arun")
    print(f"Hope you are doing well {name}")


name = input("Enter the name : ")
greet_with_name(name)


# Functions with more than one input
def greet_name_location(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}")


location = input("Enter the location : ")

greet_name_location(name, location)

print("Keyword Argument")
greet_name_location(location=location, name=name)
