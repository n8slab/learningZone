import random
import math

print("Wanna play a game... A guessing game?!")
print("How to Play:")
print("1) You select a range of numbers to guess from. Has to be range of 10 or more")
print("2) The Game will autocalculate how many guess you get")
print("3) Go hard or go home...or both, I guess? Idk I'm a computer")
print("\n \n Alright, That was a mouthful lol")

resp1attempts = 0

while resp1attempts<3:
    userReady = input("You ready to play or what?: (Yeah/Nah)\n")
    if userReady not in ("Yeah", "yeah", "Yes", "yes", "Nah", "nah", "No", "no"):
        resp1attempts+=1
        if resp1attempts>=3:
            print("Well this is going nowhere... Come back when you're ready")
            quit()
        print("Uh...I don't think I understand")
        continue
    elif userReady in ("Nah", "nah", "No", "no"):
        print("No worries bro. Come back when you're ready. Goodbye!")
        quit()
    elif userReady in ("Yeah", "yeah", "Yes", "yes"):
        print("Nice! Lets get it set up!")
        break

resp2attempts = 0

while resp2attempts<4:
    lowerBound = int(input("What would you like the lower bound to be?\n"))
    upperBound = int(input("What would you like the upper bound to be?\n"))
    resp2attempts+=1
    # validate inputs
    if upperBound<lowerBound or (upperBound-lowerBound)<10:
        if resp2attempts>=4:
            print("Well this is going nowhere... Come back when you're ready")
            quit()
        print("Invalid inputs. Let's try this again shall we?")
        continue
    elif lowerBound<upperBound and (upperBound-lowerBound)>=10:
        print("Sounds good!")
        break

# Calculate appropriate guesses by using following formula
# Min number of guessing = log2(upper bound - lower bound +1)
chances = int(round(math.log2(upperBound-lowerBound+1)))
number_to_guess = random.randrange(lowerBound, upperBound)

print(f"You have {chances} chances to guess the mystery number between {lowerBound} and {upperBound}. \n Ready?\n Let's begin!")

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
