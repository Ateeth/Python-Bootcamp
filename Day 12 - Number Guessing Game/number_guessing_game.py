import random

def check_guess(answer , guess) :
    if guess > answer :
        return "Too high."
    if answer > guess :
        return "Too low."
    return "Equal"

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard' :
    attempts = 5
else :
    attempts = 10

is_game_over = False
correct_guess = False
answer = random.randint(1,101)

while not is_game_over :
    print(f"You have {attempts} remaing to guess the number.")
    guess = int(input("Make a guess : "))
    result = check_guess(answer , guess)

    if result == "Equal" :
        print("Congratulations you have guessed the number correctly")
        correct_guess = True
        is_game_over = True
    else :
        print(result)
        print("Guess again.")
        attempts -= 1
        if attempts == 0 :
            is_game_over = True

if correct_guess == False :
    print(f"The number was not guessed correctly. The answer is {answer}")