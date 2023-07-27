num_char = len(input("What is your name : "))

## Find type of variable
print(type(num_char))

## Convert integer to string
str_num_char = str(num_char)
print(type(str_num_char))

## integer to float
float_num_char = float(num_char)
print(type(float_num_char))

print(70 + float("100.5"))  ## 170.5

print(str(70) + str(100)) ##70100 as concatenation