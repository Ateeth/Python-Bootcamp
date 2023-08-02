from replit import clear

# HINT: You can call clear() to clear the output in the console.
names_bids = {}

from art import logo

print(logo)

print("Welcome to the secret auction program.")

response = 'yes'

while response == 'yes':
    name = input("Enter your name?: ")
    bid = float(input("What's your bid?: $"))

    names_bids[name] = bid

    response = input("Are there any other bidders? Type 'yes' or 'no'. ")

    clear()

max_bid = 0
winner = 0

for key in names_bids:
    if max_bid < names_bids[key]:
        max_bid = names_bids[key]
        winner = key

print(f"Winner of the auction is {winner} with a bid of {max_bid}")