import time
import random


board = [' - ', ' - ', ' - ',
         ' - ', ' - ', ' - ',
         ' - ', ' - ', ' - ']

board2 = [' 1 ', ' 2 ', ' 3 ',
          ' 4 ', ' 5 ', ' 6 ',
          ' 7 ', ' 8 ', ' 9 ']


def game_mode():
    print("* * " * 12 + " \033[1;35m Welcome to TIC TAC TOE GAME \033[0m  " + "* * " * 12)
    print(" " * 6 + "Press [1] for Single-Player" + " " * 9 + "Press [2] for MultiPlayer")
    mode = int(input("  -----> "))

    if mode == 2:
        p1 = input("  Enter username for player 1: ").upper()  # capitalized
        p2 = input("  Enter username for player 2: ").upper()
        return p1, p2, mode
    else:
        if mode == 1:
            p1 = input("  Enter username for player 1: ").upper()
            p2 = "PC"
            return p1, p2, mode


class TicTacToe:
    def __init__(self, current_player, player_1, player_2, mode_,  board_1, board_2):
        self.currentPlayer = current_player
        self.Player1 = player_1
        self.Player2 = player_2
        self.mode = mode_
        self.winner = None
        self.gameRunning = True
        self.board1 = board_1
        self.board2 = board_2

    def print_board(self):  # this is for the main board of the game
        print(self.board1[0] + " | " + self.board1[1] + " | " + self.board1[2])
        print("-" * 15)
        print(self.board1[3] + " | " + self.board1[4] + " | " + self.board1[5])
        print("-" * 15)
        print(self.board1[6] + " | " + self.board1[7] + " | " + self.board1[8])

    def print_board2(self):  # this is for the basis
        print(self.board2[0] + " | " + self.board2[1] + " | " + self.board2[2])
        print("-" * 15)
        print(self.board2[3] + " | " + self.board2[4] + " | " + self.board2[5])
        print("-" * 15)
        print(self.board2[6] + " | " + self.board2[7] + " | " + self.board2[8])
        print()

    def intro(self):
        input("* * " * 14 + " \033[1;31m Press Enter   \033[0m" + "* * " * 14 + "\n")
        time.sleep(0.5)  # delays next execution to 1/2 second
        message = ("\033[93mMechanics:\033[0m Each turn will enter a number from 1 to 9 "
                   "(Please refer to the illustration above). "
                   "The first player to get\n\t\t\t3 of its marks in a row (up, down and diagonal) is the WINNER!\n "
                   "\nARE YOU READY \033[1;34m" + self.Player1 + "\033[0m and \033[1;31m" + self.Player2 + "\033[0m ?")
        self.print_board2()
        print("\n" + message + "\n" + "* * " * 32)
        input("    " * 13 + " \033[0;31m Press Enter to start   \033[0m\n")
        time.sleep(1)  # delays 1 second before the game started

    def player_input(self):
        user_inp = 0
        while True:
            if self.currentPlayer == ' X ' or self.mode == 1 == 2:
                user_inp = int(input("Enter a number 1-9 \033[1;34m" + self.Player1 + "\033[0m : "))
            elif self.currentPlayer == ' X ' or self.mode == 2:
                user_inp = int(input("Enter a number 1-9 \033[1;31m" + self.Player2 + "\033[0m : "))
            else:
                if self.mode == 1:
                    print("Enter a number 1-9 \033[1;31m" + self.Player2 + "\033[0m : ", end="")
                    time.sleep(0.5)
                    current_number = random.randint(1, 9)
                    user_inp = current_number
                    print(user_inp)
                    time.sleep(1)
            if 1 <= user_inp <= 9 and self.board1[user_inp - 1] == ' - ':
                self.board1[user_inp - 1] = self.currentPlayer  # changes the " - " (board) to either X or O
                break
            elif user_inp < 1 or user_inp > 9:
                print("Oops! Enter 1 - 9 numbers only. Try again!")
            else:
                if self.currentPlayer == ' X ':
                    print("Oops! This position is already marked. Try again \033[1;34m" + self.Player1 + "\033[0m !")
                else:
                    print("Oops! This position is already marked. Try again \033[1;31m" + self.Player2 + "\033[0m !")
            self.print_board()

    # Switch the player
    def switch_player(self):
        if self.currentPlayer == ' X ':
            self.currentPlayer = ' 0 '
        else:
            self.currentPlayer = ' X '

    # Check for wins
    # Check if there is a vertical win
    def check_vertical(self):
        if ((self.board1[0] == self.board1[3] == self.board1[6] and self.board1[0] != " - ")
                or (self.board1[1] == self.board1[4] == self.board1[7] and self.board1[1] != " - ")
                or (self.board1[2] == self.board1[5] == self.board1[8] and self.board1[2] != " - ")):
            self.winner = self.currentPlayer
            return True

    # Check if there is a Horizontal win
    def check_horizontal(self):
        if ((self.board1[0] == self.board1[1] == self.board1[2] and self.board1[0] != " - "
             or self.board1[3] == self.board1[4] == self.board1[5] and self.board1[3] != " - "
             or self.board1[6] == self.board1[7] == self.board1[8] and self.board1[6] != " - ")):
            self.winner = self.currentPlayer
            return True

    # Check if there is a Diagonal win
    def check_diagonal(self):
        if ((self.board1[0] == self.board1[4] == self.board1[8] and self.board1[0] != " - "
             or self.board1[2] == self.board1[4] == self.board1[6] and self.board1[2] != " - ")):
            self.winner = self.currentPlayer
            return True

    # Checks who win
    def check_win(self):
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal():
            player_symbols = {' X ': self.Player1, ' 0 ': self.Player2}
            print(f"\n \033[93m The WINNER is {player_symbols[self.winner]} \033[0m\n")
            return True

    # Checks if the board is full or tie
    def check_tie(self):
        # checks if all the list in the variable Board not equal to " - ".then, return true. Otherwise, return false
        return all(spot != " - " for spot in self.board1)

    # highlights the board with color of the winner
    def color_change(self):
        color = {' X ': "\033[1;34m X \033[0m", ' 0 ': "\033[1;31m 0 \033[0m"}
        if self.board1[0] == self.board1[4] == self.board1[8] == self.winner:
            self.board1[0] = self.board1[4] = self.board1[8] = color[self.currentPlayer]
        elif self.board1[2] == self.board1[4] == self.board1[6] == self.winner:
            self.board1[2] = self.board1[4] = self.board1[6] = color[self.currentPlayer]
        if self.board1[0] == self.board1[1] == self.board1[2] == self.winner:
            self.board1[0] = self.board1[1] = self.board1[2] = color[self.currentPlayer]
        elif self.board1[3] == self.board1[4] == self.board1[5] == self.winner:
            self.board1[3] = self.board1[4] = self.board1[5] = color[self.currentPlayer]
        elif self.board1[6] == self.board1[7] == self.board1[8] == self.winner:
            self.board1[6] = self.board1[7] = self.board1[8] = color[self.currentPlayer]
        if self.board1[0] == self.board1[3] == self.board1[6] == self.winner:
            self.board1[0] = self.board1[3] = self.board1[6] = color[self.currentPlayer]
        elif self.board1[1] == self.board1[4] == self.board1[7] == self.winner:
            self.board1[1] = self.board1[4] = self.board1[7] = color[self.currentPlayer]
        elif self.board1[2] == self.board1[5] == self.board1[8] == self.winner:
            self.board1[2] = self.board1[5] = self.board1[8] = color[self.currentPlayer]

    # Check if it's a tie and will stop the game
    def game_stop(self):
        if " - " not in self.board1:
            print("\n" + "* * " * 26, "\n")
            self.print_board()
            self.gameRunning = False  # the game will stop

    # It will restart the game depend on the user's decision
    def play_again(self):
        while True:
            inp = input(str("Do you want to try again? (\033[93mYes\033[0m or \033[1;31mNo\033[0m) ")).lower()
            if inp == "yes":
                self.board1 = [" - "] * 9  # Reset the board. make another the same list of variable Board
                self.currentPlayer = ' X '  # Start the next game with Player 1
                self.check_tie()
                break
            elif inp == "no":
                self.game_stop()
                self.gameRunning = False
            else:
                print("\n" + " *" * 18 + " Please answer \033[93mYes\033[0m or \033[1;31mNo\033[0m only!" + " *" * 18)
                continue
            break

    def main(self):
        while self.gameRunning:
            self.print_board()
            self.player_input()
            if self.check_win():
                self.color_change()
                self.print_board()
                self.play_again()
            elif self.check_tie():
                print("\n\033[91m It's a TIE! The board is full. \033[0m")
                self.print_board()
                self.play_again()
            else:
                self.switch_player()

        print("\n" + "* * " * 10 + "THANK YOU FOR PLAYING! " + "* * " * 10)


player1, player2, modes = game_mode()

game = TicTacToe(" X ", player1, player2, modes, board, board2)
game.intro()
game.main()
