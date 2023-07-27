#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

## Take the bill amount
total_bill = float(input("What is the total bill : $"))
ppl = int(input("How many people is the bill split between : "))
tip_per = float(input("Enter the tip percentage : "))

per_person = (total_bill / ppl) * (1 + (tip_per/100))
print(f"Amount to be paid by each person is {round(per_person,2) : .2f}")