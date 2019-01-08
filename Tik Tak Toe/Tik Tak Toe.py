#Kyle Baldwin
#4-5 12/10/18

#GLOBAL
X="X"
O="O"
EMPTY=""
TIE="TIE"
NUM_SQUARES=9



#functions
def display_instuct():
    """Display game instruction"""
    print(
    """
    Welcome to the Tic Tac Toe.
    To play you will enter a number between 0-8. The number will correspond to the board position as illustrated:

            0|1|2
            -----
            3|4|5
            -----
            6|7|8
    """)

##############################################################
def ask_yes_no(question):
    """Ask a yes or no question"""
    response=None
    while response not in ("y","n"):
        response=input(question+"y or n").lower()
    return response
#############################################################
def ask_number(question,low,high):
    """Ask for a number within a range"""
    responce="9999"
    while True:
        if responce.isdigit():
            if int(responce in range(low,high)):
                   break
            else:
                responce=input(question)
        else:
            print("you must enter a number")
            responce=input(question)
        return int(responce)
############################################################
def pieces():
    """Determine if player or computer goes first."""
    go_first=ask_yes_no("Do you want to go first?")
    if go_first=="y":
        print("\nI don't need to go first to win")
        human=X
        computer=O
    else:
        print("\nCool this will make me win faster")
        computer=X
        human=O
    return computer, human
############################################################
def new_board():
    """Create new game board"""
    board=[]
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
###########################################################
def display_board(board):
    """Display game board on screen."""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","__________")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t","__________")
    print("\t",board[6],"|",board[7],"|",board[8])
############################################################
def legal_moves(board):
    """Create list of legal moves."""
    move=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            move.append(square)
    return move
############################################################
def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
        
    if EMPTY not in board:
        return TIE
    
    return None
#############################################################
def human_move(board):
    """Get human move."""
    legal= legal_moves(board)
    move=None
    while move not in legal:
        move=num= ask_number("where would you move? (0-8)",0,NUM_SQUARES)
        if move not in legal:
            print("That was a stupid move")
    print("Fine...")    
    return move
###############################################################
def next_turn(turn):
    """Switch turns"""
    if turn==X:
        return O
    else:
        return X
################################################################
def congrat_winner(the_winner,computer,human):
    """Congratulate the winner"""
    if the_winner !=TIE:
        print(the_winner,"won!\n")
    else:
        print("It's a tie!\n")
    if winner==computer:
        print("That was easy")
    elif winner==human:
        print("I will win next time")
    elif winner ==TIE:
        print("It won't be like that next time")
##############################################################
def computer_move(board,computer,human):
    """Make computer move."""
    #make copy to work with since function
    board=board[:]
    #the best positions to have, in order
    BEST_MOVES=(4,0,2,8,1,3,5,7)

    #if computer can win take the move
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move]=EMPTY
    
    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
        board[move]=EMPTY
    #since no one can win on next move pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
############################################################
##def main():
##    display_instuct()
##    computer, human=pieces()
##    turn=X
##    board=new_board()
##    display_board(board)
##    
##    while not winner(board):
##        if turn==human:
##            move=human_move(board)
##            board[move]=human
##        else:
##            move=computer_move(board,computer,human)
##            board[move]=computer
##        display_board(board)
##        turn=next_turn(turn)
##    the_winner=winner(board)
##    congrat_winner(the_winner,computer,human)
##
##main()
board=X,X,X,O,O,O,O,O,O
display_board(board)

















        

        
        
    
            
    
            
            
    
