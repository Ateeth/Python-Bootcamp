programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieve values from dictionary
print(programming_dictionary["Bug"])

# Get keys of dictionary
print("Keys in the dictionary")
for key in programming_dictionary :
    print(key)

# Get all the values in the dictionary
print("Values of the dictionary")
for key in programming_dictionary :
    print(programming_dictionary[key])

# Add new entry to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)