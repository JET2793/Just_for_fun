
from random import randint

play=0
play_limit=3

for play in range(play_limit):
    if play==0:
        print("*** Welcome to Battleships! ***")
    else:
        print("---------------------")
        print("Let's try again then!")
    play+=1
    board = []
    #Making 5x5 board
    for x in range(5):
        board.append(["O"] * 5)
    #Defining print layout to remove ""
    def print_board(board):
        for row in board:
            print ("        "+" ".join(row))
    print("  ")
    print("Here's the current board:")
    print("  ")
    print_board(board)
    
    def random_row(board):
        return randint(0, len(board) - 1)
    
    def random_col(board):
        return randint(0, len(board[0]) - 1)
    
    #Randomly placing battleship position
    ship_row = random_row(board)
    ship_col = random_col(board)
    # print (ship_row)
    # print (ship_col)
    
    # Setting number of turns permitted
    turn_limit=3
    for turn in range(turn_limit):
        print("  ")
        print ("Turn "+str(turn+1)+"/"+str(turn_limit))
        # Asking for user guess
        guess_row = int(input("Guess row position (1-5): "))-1
        guess_col = int(input("Guess column position (1-5): "))-1
        # If user guess correct, breaking loop
        print ("  ")
        if guess_row == ship_row and guess_col == ship_col:
            print ("Congratulations! You sunk the battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that position before.")
            else:
                print ("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                # print (turn+1)

        if turn==(turn_limit-1):
            print("-------------------------")
            print ("Out of turns! Game Over :(")
            print("The battleship was here:")
            board[ship_row][ship_col] = "S"
            print (" ")
            print_board(board)
            print (" ")
        else:
            #print("-------------------------")
            print("Try again. Here's the current board:")
            print (" ")
            print_board(board)
            print (" ")
    
    if play < play_limit:
        play_again= str(input("Play again? (y/n): "))
        while play_again != "y" and play_again !="n":
            play_again= str(input("Invalid input! Play again? (y/n): "))
        if play_again == "y":
            play+=1
        elif play_again == "n":
            print ("OK, fair enough. Goodbye!")
            break
 
    else:
        print ("You should probably try a new game now. Bye!")
        
