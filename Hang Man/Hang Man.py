#Kyle Baldwin
#Hang man game
#11/26/18

#import
import random
import time

#constants
HANGMAN=(
'''

 ------
 |    |
 |    |
 |    
 |
 |
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |
 |
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |    +
 |
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |    +\
 |
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |   /+\
 |
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |   /+\
 |    +
 |
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |   /+\
 |    +
 |     \
 |
 |
-------
''',
'''

 ------
 |    |
 |    |
 |    0
 |   /+\
 |    +
 |   / \
 |
 |
-------
''')

MAX_WRONG=len(HANGMAN)-1
WORDS=("PYTHON","INDEX","STRING","INTEGER","FLOAT","FUNCTION","BREAK","IF","WHILELOOP","PRINT")

word=random.choice(WORDS)#The word to be guessed
so_far=" _ "*len(word)#one dash for eash in word to be guessed
wrong=0# number of wrong guesses
used=[]#letters already guessed 

def hangman():
    global HANGMAN
    global word
    global so_far
    global wrong
    global used
    global MAX_WRONG
    global WORDS
    print("Welcome to hangman. Good Luck!")
    while wrong<MAX_WRONG and so_far!=word:

        print(HANGMAN[wrong])
        print("\nYou've used to following letters:\n",used)
        print("\nSo far, the word is :\n",so_far)

        guess=input("\n\nEnter your guess:")
        guess=guess.upper()


        while guess in used:
            print("You already guessed the letter",guess)
            guess=input("\n\nEnter your guess:")
            guess=guess.upper()

        used.append(guess)

        if guess in word:
            print("\nYes!",guess,"is in the word!")

            #create a new so_far to include guess
            new=""
            for i in range(len(word)):
                if guess==word[i]:
                    new+=guess
                else:
                    new+=so_far[i]
            so_far=new
        else:
            print("\nSorry,",guess,"isn't in the word.")
            wrong+=1

    if wrong==MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")

    else:
        print("\n guessed it!")
    print("\nThe word was",word)
    input("\n\nPress the enter key to exit")
hangman()
          




















                








        
    



    


