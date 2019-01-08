import random
import time

global low
global high
global guess

low = 1
high = 100
random_num = 5



print("Welcome to the Guessing Game!")
print()

print("Here are your options:")
print()

print("Play: You have five guesses to correctly guess a random number picked from a range of 1 to 100.")
print()

print("Advanced: Pick the number range or how many guesses you can start with.")
print()

print("Credits: Shows who made the game.")
print()

print("Quit: Closes the program.")
print()

choice = input("Please choose an option. ")
print()


def game():
    i = 0
    while i !=5:
        guess_1=int(input("Guess a number between 1 and 100"))
        if guess_1==random_num:
            print("Your Correct")
            print("You Win")
            break
        elif guess_1>random_num:
            print("The number that you guessed is higher then then random number")
            i+=1
        elif guess_1<random_num:
            print("The number that you guessed is lower then then random number")
            i+=1
            if i==5:
                print("You Lose")
                time.sleep(5)
        else:
            print("This is not a valid number please try again")
            

def advanced():
    while True:
        choice = input("Would you like to change the number range (N) or the amount of guesses (G)? ")
        print()
        if choice.lower().startswith("n"):
            low = input("Please set the lowest number: ")
            print()
            if low.isdigit():
                high = print("Please set the highest number: ")
                print()
                if high.isdigit() and high > low:
                    game()
                    break
                else:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
            else:
                print("Please input a valid number.")
                print()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit():
                game()
                break
            else:
                print("Please input a valid integer.")
                print()
    return


while True:
    if choice.lower().startswith("p"):
        game()
        print()
        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
    elif choice.lower().startswith("a"):
        advanced()
        print()
        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
    elif choice.lower().startswith("c"):
        print("The Guessing Game.")
        print()

        print("Created by \nKyle Baldwin \nMichael Freeman")
        print()

        print("Game design by \nKyle Baldwin")
        print()

        print("Advanced Options by \n Michael Freeman")
        print()

        print("Created in Python")
        print()

        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")
        print()
    elif choice.lower().startswith("q"):
        print("Thank you for playing!")
        time.sleep(3)
        exit()
    else:
        print("That is not a option try again")
        print()
        choice = input("What would you like to do now? Play, Advanced, Credits or Quit? ")

        
