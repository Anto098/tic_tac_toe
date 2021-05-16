import os
import sys
clear = lambda: os.system("cls")#clear function, clears the console screen
board = [" "," "," "," "," "," "," "," "," "]#Initialize global variables
turn = 0
player1_score=0
player2_score=0

def main():#core loop of the game, displays the beginning screen, calls other functions and displays the result of the game
    print("\nWelcome to Tic Tac Toe! To play: Place your symbol ('X' for Player 1 and 'O' for Player 2) to form a line or diagonal of 3 symbols.")
    print("Refer to the Tic Tac Toe diagram on the right to place your symbol.")
    print("To see the rules again, type : 'Help'. To restart the game, type: 'Restart'.\nTo clear the score, type: 'Clear'. To quit, type 'Quit'. To forfeit, type: 'Forfeit'. ")
    display_board([" "," "," "," "," "," "," "," "," "])
    play_loop()
    if hasWon():
        global player1_score, player2_score
        if ((turn-1)%2)+1 == 1:#If player 1 won, increment his score
            player1_score+=1
        else:#Otherwise, increment the second player's score
            player2_score+=1
        print(f"Player {((turn-1)%2)+1} Won!")
    elif isFull():
        print("It's a tie!")
    replay()

def replay():#Asks if the players want to play again, if yes: resets variables and replays, else exits program
    replay = ""
    while replay not in ("yes","y","no","n"):
        replay = input("Do you want to play again? (yes/no) : ").lower()
        if replay in ("yes","y"):
            reset()
            main()
        elif replay in ("no","n"):
            sys.exit(0)
def reset():#resets global variables
    clear()
    global board, turn
    #Modify global variables to be able to access them later in other methods
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = 0
def display_board(board):#Displays 2 boards, the left board displays the game being played, the right board displays the position numbers
    j=0
    print(f"\n     player 1 : {player1_score}\n     player 2 : {player2_score}\n")#When running the program in an IDE (intelliJ), a special character is printed after clear(), which offsets the first print, to fix this I print an empty line
    for i in range(11):
        if i%2==0:
            print("     |   |            |   |  ")
        elif (i-1)%4 == 0:
            print(f"   {board[j]} | {board[j+1]} | {board[j+2]}        {j+1} | {j+2} | {j+3} ")
            j+=3
        else :
            print("---------------   --------------")
    print("")
def play(pos):#Plays a X or O on the grid, depending which player is playing.
    global turn
    if turn%2==0:
        board[pos-1]="X"
    elif turn%2==1:
        board[pos-1]="O"
    turn+=1
def hasWon():#Checks if a player won
    #Check diagonals
    if (board[0]==board[4]==board[8] or board[2]==board[4]==board[6]) and board[4]!=" ":
        #It would be worth it to loop on the conditions if there were more elements
        return True
    for i in range(0,3):
            #Check columns
        if (board[i] == board[i+3] == board[i+6] and board[i]!=" "):
            #I check the 2 different conditions with different statements for code readability
            return True
            #Check lines
        elif (board[i*3]==board[i*3+1]==board[i*3+2] and board[i*3]!=" "):
            return True
    return False
def isFull():#Checks if the board is full
    for i in board:
        if i == " ":
            return False
    return True
def play_loop():#Loops while game isn't over. Takes input and either: plays, clears screen and displays or: executes command
    takeUserInput()
    if not hasWon() and not isFull() :#While game isn't over, play.
        play_loop()
def takeUserInput():#Reacts to player input
    user_input = input(f"Player {(turn % 2) + 1}, select the box to place your symbol in or enter a command : ")
    if not checkValidInt(user_input):#If the user_input isn't an int, the method won't be able to treat it, so check if it's a valid command (string)
        checkValidCommand(user_input)
def checkValidInt(user_input):#If user_input is int: return True, else return False. Treat int if possible.
    try:
        user_input = int(user_input)
        if user_input not in range(1, 10) or board[user_input-1] != " ":
            # If the position is outside the grid or is already used, send error message and continue to loop
            print("Please enter a number from 1 to 9 which hasn't been used yet.")
            return True #Go back to play_loop, don't play the invalid user input
        play(user_input)
        clear()
        display_board(board)
        return True
    except ValueError: #If user_input isn't an integer:
        return False
def checkValidCommand(user_input):#If user_input is a valid command, treat it, otherwise send error message
    global player1_score, player2_score
    if user_input.lower() == "restart":
        reset()
        main()
    elif user_input.lower() == "help":
        print(" To play: Type your symbol ('X' for Player 1 and 'O' for Player 2) to form a line or diagonal of 3 symbols. \n Commands available: 'Restart', 'Help', 'Clear', 'Quit', 'Forfeit'. ")
    elif user_input.lower() == "clear":
        player1_score=0
        player2_score=0
        clear()
        display_board(board)
    elif user_input.lower() == "quit":
        sys.exit(0)
    elif user_input.lower() == "forfeit":
        if ((turn+1)%2)+1 == 1:#If player 2 forfeited, increment player1_score
            player1_score+=1
        else:                  #If player 1 forfeited, increment player2_score
            player2_score+=1
        reset()
        main()
    else:
        print("The command you entered isn't valid, try: 'Restart', 'Help', 'Clear', 'Quit' or 'Forfeit'. ")
main()
