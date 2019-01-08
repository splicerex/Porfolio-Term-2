import random
import time

random_num=(45)



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
        else:
            print("This is not a valid number please try again")

game()
           


            
                      
                      
                      
                            
                      
    
    
