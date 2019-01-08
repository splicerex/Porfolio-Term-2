#Kyle Baldwin
#1/2/19
#Trivia Game
#imports
import sys
import time
#opens the file
def open_file(file_name,mode):
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print("Unable to open the file")
        input("\nPress the enter key to exit")
        sys.exit()
    else:
        return the_file


#Reads the next line
    
def next_line(the_file):
    line=the_file.readline()
    line=line.replace("/","\n")
    return line

#all the questions, category, answers, correct answers, and the explanation
def next_block(the_file):
    category=next_line(the_file)
    
    question=next_line(the_file)
    
    answers=[]
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    
    return category, question, answers, correct, explanation

#title
def welcome(title):
    print("Welcome to Trivia Challenge!\n")
    print(title,"\n")

#main function
def main():
    file="The_file.txt"
    file_open=open_file(file,"r")
    title=next_line(file_open)
    welcome(title)
    score=0
    category, question, answers, correct, explanation=next_block(file_open)
    while category:
        time.sleep(2)
        print(category)
        print(question)
        for i in range(4):
            print(str(i),answers[i])
        answer=input("What is the correct answer")
        if answer==correct:
            print("Congrats you got it Correct")
            score+=1
        else:
            print("You got it wrong")
        print(explanation)
        print("Your score is",score)
        category, question, answers, correct, explanation=next_block(file_open)
    file_open.close()
    print("Thank you for playing this Trivia Game.")
    print("Your score was",score)

main()
input("press enter to quit")     
    












