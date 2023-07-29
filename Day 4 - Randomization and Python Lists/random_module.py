import random
import my_module
# Random integer between 1 and 10 including 1 and 10
random_integer = random.randint(1 , 10)
print(random_integer)

# Print variable pi from another file my_module.py
print(my_module.pi)

# Random float number between  0 and 1 not including 1 [0 , 1)
random_float = random.random()
print(random_float)

# Random float between 0 and 5
random_float_05 = random_float * 5
print(random_float_05)