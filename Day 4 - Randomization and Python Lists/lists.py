states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2])

# 5th element from the end
print(states_of_america[-5])

# Change elements of list
states_of_america[1] = "Pencilvania"

print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

# Append item to end of list
states_of_america.append("Ateeth Land")

# Print last element of list
print(states_of_america[-1])

# Add multiple items to the end of the list
states_of_america.extend(["A", "B", "C", "D"])
print(states_of_america)

# Insert element at custom position in list
states_of_america.insert(1, "CUSTOM")
print(states_of_america)

# Remove a particular item from list
states_of_america.remove("CUSTOM")
print(states_of_america)

# Remove an element at a given index in list
states_of_america.pop(0)
print(states_of_america)

# Remove last element from the list
states_of_america.pop()
print(states_of_america)

# Find location of item in list
print(f"LOCATION Georgia :  {states_of_america.index('Georgia')}")

# Find number of occurences of item in list
print(f"Count of Delaware {states_of_america.count('Delaware')}")

# Sort the list
states_of_america.sort()
print(states_of_america)

# Reverse the list
states_of_america.reverse()
print(states_of_america)

# Slicing the list
# Note that the end index is not included in the splice
# Print first 10 elements of list
print(f"First 10 states {states_of_america[0:10]}")

# Print last 5 elements of list
print(f"Last 5 states {states_of_america[-5:len(states_of_america)]}")

# First 5 alternate states in list i.e steps of 2
print(f"First 10 alternate states of list : {states_of_america[0:20:2]}")