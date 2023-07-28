## Refer to Rollercoaster_latest.pdf for the flowchart which has been implemented
print("Welcome to the rollercoaster")
height = float(input("What is your height in cm : "))

if height >= 120:
    print("You are allowed to enter the rollercoaster :)")
    age = int(input("Enter your age : "))
    fee = 0
    if age < 12 :
        fee = 5
    elif age <= 18 :
        fee = 7
    elif 45 <= age <= 55:
        fee = 0
    else :
        fee = 12

    want_photos = input("Do you want photos : Yes or No : ")
    if want_photos == 'Yes' :
        fee += 3
    print(f"Kindly pay the entry fee of {fee}$ to enter the rollercoaster")
else:
    print("Sorry :( You are not allowed to enter the rollercoaster")