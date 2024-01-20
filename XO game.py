import random
import time  # For delays

currentPlayer = ' X '
GameRunning = True
winner = None

print("* * " * 12 + " \033[1;35m Welcome to TIC TAC TOE GAME \033[0m  " + "* * " * 12)
print(" " * 6 + "Press [1] for Single-Player" + " " * 9 + "Press [2] for MultiPlayer")
mode = int(input("  -----> "))
Player1 = ''
Player2 = ''

# Set player names based on modes
if mode == 2:
    Player1 = input("  Enter username for player 1: ").upper()  # capitalized
    Player2 = input("  Enter username for player 2: ").upper()
else:
    if mode == 1:
        Player1 = input("  Enter username for player 1: ").upper()
        Player2 = "PC"
        print("  Enter username for player 2: PC")


input("* * " * 14 + " \033[1;31m Press Enter   \033[0m" + "* * " * 14 + "\n")
time.sleep(0.5)  # delays next execution to 1/2 second
message = ("\033[93mMechanics:\033[0m Each turn will enter a number from 1 to 9 "
           "(Please refer to the illustration above). "
           "The first player to get\n3 of its marks in a row (up, down and diagonal) is the WINNER!\n "
           "\nARE YOU READY \033[1;34m" + Player1 + "\033[0m and \033[1;31m" + Player2 + "\033[0m ?")


# Listing 9 empty spot as " - " for the board
board = [' - ', ' - ', ' - ',
         ' - ', ' - ', ' - ',
         ' - ', ' - ', ' - ']

board2 = [' 1 ', ' 2 ', ' 3 ',
          ' 4 ', ' 5 ', ' 6 ',
          ' 7 ', ' 8 ', ' 9 ']


# Printing board
def print_board(board_):  # this is for the main board of the game
    print(board_[0] + " | " + board_[1] + " | " + board_[2])
    print("-" * 15)
    print(board_[3] + " | " + board_[4] + " | " + board_[5])
    print("-" * 15)
    print(board_[6] + " | " + board_[7] + " | " + board_[8])


# This is for the basis
def print_board2(board2_):  # this is for the basis
    print(board2_[0] + " | " + board2_[1] + " | " + board2_[2])
    print("-" * 15)
    print(board2_[3] + " | " + board2_[4] + " | " + board2_[5])
    print("-" * 15)
    print(board2_[6] + " | " + board2_[7] + " | " + board2_[8])
    print()


print_board2(board2)
print("\n" + message + "\n" + "* * " * 32)
input("    " * 13 + " \033[0;31m Press Enter to start   \033[0m\n")
time.sleep(1)  # delays 1 second before the game started


# Take the player's input
def player_input():
    user_inp = 0
    while True:
        if currentPlayer == ' X ' or mode == 1 == 2:
            user_inp = int(input("Enter a number 1-9 \033[1;34m" + Player1 + "\033[0m : "))
        elif currentPlayer == ' X ' or mode == 2:
            user_inp = int(input("Enter a number 1-9 \033[1;31m" + Player2 + "\033[0m : "))
        else:
            if mode == 1:
                print("Enter a number 1-9 \033[1;31m" + Player2 + "\033[0m : ", end="")
                time.sleep(0.5)
                current_number = random.randint(1, 9)
                user_inp = current_number
                print(user_inp)
                time.sleep(1)
        if 1 <= user_inp <= 9 and board[user_inp - 1] == ' - ':
            board[user_inp - 1] = currentPlayer  # changes the " - " (board) to either X or O
            break
        elif user_inp < 1 or user_inp > 9:
            print("Oops! Enter 1 - 9 numbers only. Try again!")
        else:
            if currentPlayer == ' X ':
                print("Oops! This position is already marked. Try again \033[1;34m" + Player1 + "\033[0m !")
            else:
                print("Oops! This position is already marked. Try again \033[1;31m" + Player2 + "\033[0m !")
        print_board(board)


# Switch the player
def switch_player():
    global currentPlayer
    if currentPlayer == ' X ':
        currentPlayer = ' 0 '
    else:
        currentPlayer = ' X '


# Check for wins
# Check if there is a vertical win
def check_vertical(board_):
    global winner
    if ((board_[0] == board_[3] == board_[6] and board_[0] != " - ")
            or (board_[1] == board_[4] == board_[7] and board_[1] != " - ")
            or (board_[2] == board_[5] == board_[8] and board_[2] != " - ")):
        winner = currentPlayer
        return True


# Check if there is a Horizontal win
def check_horizontal(board_):
    global winner
    if ((board_[0] == board_[1] == board_[2] and board_[0] != " - "
         or board_[3] == board_[4] == board_[5] and board_[3] != " - "
         or board_[6] == board_[7] == board_[8] and board_[6] != " - ")):
        winner = currentPlayer
        return True


# Check if there is a Diagonal win
def check_diagonal(board_):
    global winner
    if ((board_[0] == board_[4] == board_[8] and board_[0] != " - "
         or board_[2] == board_[4] == board_[6] and board_[2] != " - ")):
        winner = currentPlayer
        return True


# Checks who win
def check_win(board_):
    if check_horizontal(board_) or check_vertical(board_) or check_diagonal(board_):
        player_symbols = {' X ': Player1, ' 0 ': Player2}  # dictionary: naming the winner instead of the "X" and "0"
        print(f"\n \033[93m The WINNER is {player_symbols[winner]} \033[0m\n")
        return True


# Checks if the board is full or tie
def check_tie():
    # checks if all the list in the variable Board not equal to " - ".then, return true. Otherwise, return false
    return all(spot != " - " for spot in board)


# Check if it's a tie and will stop the game
def game_stop():
    global GameRunning
    if " - " not in board:
        print("\n" + "* * " * 26, "\n")
        print_board(board)
        GameRunning = False  # the game will stop


# It will restart the game depend on the user's decision
def play_again():
    global board, currentPlayer, GameRunning
    while True:
        inp = input(str("Do you want to try again? (\033[93mYes\033[0m or \033[1;31mNo\033[0m) ")).lower()
        if inp == "yes":
            board = [" - "] * 9  # Reset the board. make another the same list of variable Board
            currentPlayer = ' X '  # Start the next game with Player 1
            check_tie()
            break
        elif inp == "no":
            game_stop()
            GameRunning = False
        else:
            print(" *" * 18 + " Please answer \033[93mYes\033[0m or \033[1;31mNo\033[0m only!" + " *" * 18)
            continue
        break


# The main loop of the game
while GameRunning:
    print_board(board)
    player_input()
    if check_win(board):
        print_board(board)
        play_again()
    elif check_tie():
        print("\n\033[91m It's a TIE! The board is full. \033[0m")
        print_board(board)
        play_again()
    else:
        switch_player()

print("\n" + "* * " * 10 + "THANK YOU FOR PLAYING! " + "* * " * 10)
