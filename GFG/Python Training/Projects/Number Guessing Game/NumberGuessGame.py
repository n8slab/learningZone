import random

print("Wanna play a game... A guessing game?!")
print("You have 7 chances to guess the number. Ready?\n Let's begin!")

# first need to create vars for num chances and the actual number to be guessed
number_to_guess = random.randrange(1, 100)

chances = 7
chanceCounter = 0

# make loop that closes if too many guesses OR guess correctly

while chanceCounter < chances:
    #incriment chanceCounter and ask for user input. Typecast input to integer
    chanceCounter+=1
    user_guess = int(input('Enter your guess: '))

    if user_guess==number_to_guess:
        print(f"That's right! The correct answer was {number_to_guess} and you got it right in only {chanceCounter} attempts!")
        break
    elif chanceCounter>=chances and user_guess!=number_to_guess:
        print("Yikes...sorry bud. Thats the wrong answer!\n Your're out of chances but BETTER LUCK NEXT TIME!")
    elif user_guess<number_to_guess:
        print("Too low! Guess again")
    elif user_guess>number_to_guess:
        print("Too high! Guess again")
