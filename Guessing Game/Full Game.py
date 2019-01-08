import random
import time

low = 1
high = 100
guess = 5


#Menu

def menu():

    print("Welcome to the Guessing Game!")
    print()
    
    print("Here are your options:")
    print()
    
    print("Play: You have five guesses to correctly guess a random number picked from a range of 1 to 100.")
    print()
    
    print("Advanced: Pick the number range or how many guesses you can start with.")
    print()

    print("Another Game: Crossword game")
    print()
    
    print("Credits: Shows who made the game.")
    print()
    
    print("Quit: Closes the program.")
    print()
    
    choice = input("Please choose an option. ")
    print()

    low = 1
    high = 100
    guess = 5

    
    while True:
        if choice.lower().startswith("play"):
            return game_1(),low,high,guess
        elif choice.lower().startswith("advanced"):
            return advanced()
        elif choice.lower().startswith("credit"):
            return credit()
        elif choice.lower().startswith("another game"):
            return word_1()
        elif choice.lower().startswith("quit"):
            print("Thank you for playing!")
            time.sleep(2)
            exit()
        else:
            print("That is not a option try again")
            print()
            print()
            time.sleep(1)
            return menu()

#Credits

def credit():
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
    print()
    time.sleep(2)

    return menu()



#Advanced game 

def advanced():
    global high
    global low
    global guess
    low = 1
    high = 100
    guess = 5
    while True:
        choice = input("Would you like to change the number range (N) or the amount of guesses (G)? ")
        print()
        if choice.lower().startswith("n"):
            low = input("Please set the lowest number: ")
            print()
            if low.isdigit() is True:
                high = input("Please set the highest number: ")
                print()
                if high.isdigit() is True and high > low:
                    game_2()
                    break
                if high.isdigit() is False:
                    print("Please input a valid number or choose a number higher than the lower number.")
                    print()
                    return advanced()
            if low.isdigit() is False:
                print("Please input a valid number.")
                print()
                return advanced()
        elif choice.lower().startswith("g"):
            guess = input("Please set the number of guesses. ")
            print()
            if guess.isdigit() is True:
                game_2()
                break
            if guess.isdigit() is False:
                print("Please input a valid integer.")
                print()
                print()
            return advanced()
    


#Main Game

def game_1():
    global low
    global high
    global guess
    global random_num
    low=1
    high=100
    guess=5
    low = int(low)
    high=int(high)
    random_num = random.randrange(low,high)
    guess = int(guess)
    guess_num = 0
    while guess_num != guess:
        print('Guess a number between',low,'and',high,'.')
        guess_1=input("Guess a number")
        if guess_1.isdigit() is True:
            if int(guess_1)==random_num:
                print("You're Correct")
                print("You Win the number was",str(random_num),".")
                print()
                print()
                time.sleep(2)
                return menu()
            elif int(guess_1)>random_num:
                print("The number that you guessed is higher then then random number")
                guess_num+=1
                print(guess_num,"out of",guess, "you have done")
                print()
            elif int(guess_1)<random_num:
                print("The number that you guessed is lower then then random number")
                guess_num+=1
                print(guess_num,"out of",guess,"you have done")
                print()
        if guess_1.isdigit() is False:
            print("This is not a valid number please try again")
            
    print("You Lose the number was",str(random_num),".")
    print()
    print()
    time.sleep(2)
    return menu()

#Advanced Game i had to do this to fix a logical error

def game_2():
    global low
    global high
    global guess
    global random_num
    low = int(low)
    high=int(high)
    random_num = random.randrange(low,high)
    guess = int(guess)
    guess_num = 0
    while guess_num != guess:
        print('Guess a number between',low,'and',high,'.')
        guess_1=input("Guess a number")
        if guess_1.isdigit() is True:
            if int(guess_1)==random_num:
                print("You're Correct")
                print("You Win the number was",str(random_num),".")
                print()
                print()
                time.sleep(2)
                return menu()
            elif int(guess_1)>random_num:
                print("The number that you guessed is higher then then random number")
                guess_num+=1
                print(guess_num,"out of",guess, "you have done")
                print()
            elif int(guess_1)<random_num:
                print("The number that you guessed is lower then then random number")
                guess_num+=1
                print(guess_num,"out of",guess,"you have done")
                print()
        if guess_1.isdigit() is False:
            print("This is not a valid number please try again")
            
    print("You Lose the number was",str(random_num),".")
    print()
    print()
    time.sleep(2)
    return menu()






puzzle=("SFXAGTNIRPEUIVZJAXEPLNKAERBTGFBCJFLOATESATCFWSJWTTIIOCIMBNN"+
                    "RROKDBRKDIIANMMUAQYXNVNOHTYPIFGYWHILELOOP")

#Display the puzzle to make look better
display_puzzle=('''
  |0|1|2|3|4|5|6|7|8|9|
00|S|F|X|A|G|T|N|I|R|P|
10|E|U|I|V|Z|J|A|X|E|P|
20|L|N|K|A|E|R|B|T|G|F|
30|B|C|J|F|L|O|A|T|E|S|
40|A|T|C|F|W|S|J|W|T|T|
50|I|I|O|C|I|M|B|N|N|R|
60|R|O|K|D|B|R|K|D|I|I|
70|A|N|M|M|U|A|Q|Y|X|N|
80|V|N|O|H|T|Y|P|I|F|G|
90|Y|W|H|I|L|E|L|O|O|P|    ''')

#point system
point=0
def point_system():
    global point
    print("You got",point,"points")
    return menu()


#word 1 guess and search
def word_1():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("what is a programing language").lower()
        attempt+=1
        print(attempt)
        if guess=="python":
            print("You are correct")  
            word1_length=len("python")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==14:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="PYTHON":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_2()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")
            


#word 2 guess and search
def word_2():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("What is it called when a number has a decimal in it").lower()
        attempt+=1
        print(attempt)
        if guess=="float":
            print("You are correct")  
            word1_length=len("Float")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==10:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="FLOAT":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_3()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 3 guess and search
def word_3():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("Another word for numbers").lower()
        attempt+=1
        print(attempt)
        if guess=="integer":
            print("You are correct")  
            word1_length=len("integer")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==14:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="INTEGER":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_4()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")

            
#word 4 guess and search
def word_4():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("What is it called when you defin something").lower()
        attempt+=1
        print(attempt)
        if guess=="function":
            print("You are correct")  
            word1_length=len("Function")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==16:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="FUNCTION":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_5()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 5 guess and search
def word_5():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("Stops While loops").lower()
        attempt+=1
        print(attempt)
        if guess=="break":
            print("You are correct")  
            word1_length=len("break")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==10:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="BREAK":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_6()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 6 guess and search
def word_6():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("Used to determine, which statements are going to be executed").lower()
        attempt+=1
        print(attempt)
        if guess=="if":
            print("You are correct")  
            word1_length=len("if")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==4:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="IF":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_7()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 7 guess and search
def word_7():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("Loop multiple times until you tell it to stop(one long word)").lower()
        attempt+=1
        print(attempt)
        if guess=="whileloop":
            print("You are correct")  
            word1_length=len("whileloop")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==18:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="WHILELOOP":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_8()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 8 guess and search
def word_8():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("display words").lower()
        attempt+=1
        print(attempt)
        if guess=="print":
            print("You are correct")  
            word1_length=len("print")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==10:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="PRINT":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_9()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 9 guess and search
def word_9():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("reserved memory locations to store values").lower()
        attempt+=1
        print(attempt)
        if guess=="variable":
            print("You are correct")  
            word1_length=len("Variable")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==16:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="VARIABLE":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return word_10()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")



#word 10 guess and search
def word_10():
    global puzzle
    global point
    i=0
    attempt=0
    while i==0:
        #Question
        guess=input("sequence of characters	").lower()
        attempt+=1
        print(attempt)
        if guess=="string":##
            print("You are correct")  
            word1_length=len("string")
            print(display_puzzle)
            x=0
            while x==0:
                #WordSearch
                word1=input("where is the word")
                i=0
                if len(word1)==12:
                    if word1.isdigit():
                        attempt+=1
                        foundword=""
                        while i < word1_length*2:
                            index1=word1[i]
                            index2=word1[i+1]
                            index=index1+index2
                            index=int(index)
                            foundword=foundword+puzzle[index]
                            i+=2
                            print(foundword)
                        if foundword=="STRING":
                            print(foundword)
                            print("Great Job")
                            #Points system
                            if attempt==2 or attempt==3:
                                point+=10
                            elif attempt==4 or attempt==5:
                                point+=9
                            elif attempt==5 or attempt==6:
                                point+=8
                            elif attempt==7 or attempt==8:
                                point+=7
                            elif attempt==9 or attempt==10:
                                point+=6
                            elif attempt==11 or attempt==12:
                                point+=5
                            elif attempt==13 or attempt==14:
                                point+=4
                            elif attempt==15 or attempt==16:
                                point+=3
                            elif attempt==17 or attempt==18:
                                point+=2
                            elif attempt==19 or attempt==20:
                                point+=1
                            else:
                                point+=0
                            print(attempt)
                            x=1
                            return point_system()
                        else:
                            print("thats not right try agian")
                    else:
                        print("This is not a number")
                else:
                    print("This number is not long enough")
        else:
            print("you are wrong")







menu()






        
