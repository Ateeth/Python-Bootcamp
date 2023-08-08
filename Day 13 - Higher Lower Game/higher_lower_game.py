from art import logo, vs
from game_data import data
import random

def check_answer(guess, p1_followers, p2_followers) :
    if guess == 'A' :
        if p1_followers >= p2_followers :
            return True
    elif guess == 'B' :
        if p2_followers >= p1_followers :
            return True
    return False

print(logo)
isGameOver = False
score = 0


p1 = random.randint(0 , len(data) - 1)

while not isGameOver :
    p2 = p1
    while p2 == p1 :
        p2 = random.randint(0,len(data) - 1)

    person1 = data[p1]
    person2 = data[p2]

    print(f"Compare A : {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)
    print(f"Compare B : {person2['name']}, a {person2['description']}, from {person2['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if check_answer(user_choice, person1['follower_count'], person2['follower_count']) == True :
        score = score + 1
        print(f"You're right! Current score: {score}.")
        p1 = p2

    else :
        isGameOver = True
        print(f"Sorry, that's wrong. Final score: {score}")