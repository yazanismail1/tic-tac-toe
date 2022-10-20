import random
import re
# import numpy as np


class TicTacToe:
    def __init__(self):
        self.available_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # self.turns_tracker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.playing_board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]]
        self.position_on_board = {
            "1": {'i':0, "j":0},
            "2": {'i':0, "j":1},
            "3": {'i':0, "j":2},
            "4": {'i':1, "j":0},
            "5": {'i':1, "j":1},
            "6": {'i':1, "j":2},
            "7": {'i':2, "j":0},
            "8": {'i':2, "j":1},
            "9": {'i':2, "j":2},
        }
        self.board = """
      1  |  2  |  3 
    -----------------
      4  |  5  |  6 
    -----------------
      7  |  8  |  9 
    """

    def __str__(self):
        welcome_message = """
    -----------------------
    Welcome to Tic Tac Toe
    -----------------------
    It is simple, you will be asked to enter a the 
    number you want to place you sign.

    You will be playing against a bot, you will take (X),
    and the bot will be (O).

    Rules to win -->

    1. Place three horizontal (X) signs.
    2. Place three vertical (X) signs.
    3. Place three diagonal (X) signs.
    -----------------------

    """
        return welcome_message

    def update_visual_board(self, position, sign):
        self.board = re.sub(position, sign, self.board)

    def check_available_spots(self, position):
        if position in self.available_spots:
            return True
        else:
            return False

    # def check_turns(self):
    #     if self.turns_tracker[0]%2 == 0:
    #         self.turns_tracker.pop(0)
    #         return "bot"
    #     else:
    #         self.turns_tracker.pop(0)
    #         return "user"

    def update_available_spots(self, position):
        for i in self.available_spots:
            if str(i) == position:
                self.available_spots.remove(i)

    def update_playing_board_user(self, position):
        self.playing_board[self.position_on_board[position]["i"]][self.position_on_board[position]["j"]] = "X"
        self.update_available_spots(position)
        
    def update_playing_board_bot(self):
        try:
            position = str(random.choice(self.available_spots))
            self.playing_board[self.position_on_board[position]["i"]][self.position_on_board[position]["j"]] = "O"
            self.update_available_spots(position)
            self.update_visual_board(position, "O")
        except IndexError:
            pass

    def check_winner(self):
        if ["X","X","X"] in self.playing_board:
            print("You Won...")
            return True
        if ["O","O","O"] in self.playing_board:
            print("You Lost...")
            return True
        if self.playing_board[0][0] == self.playing_board[1][1] and self.playing_board[0][0] == self.playing_board[2][2]:
            if self.playing_board[0][0] == "X":
                print("You Won...")
                return True
            if self.playing_board[0][0] == "O":
                print("You Lost...")
                return True
        if self.playing_board[0][2] == self.playing_board[1][1] and self.playing_board[0][2] == self.playing_board[2][0]:
            if self.playing_board[0][2] == "X":
                print("You Won...")
                return True
            if self.playing_board[0][2] == "O":
                print("You Lost...") 
                return True
        if self.playing_board[0][0] == self.playing_board[1][0] and self.playing_board[0][0] == self.playing_board[2][0]:
            if self.playing_board[0][0] == "X":
                print("You Won...")
                return True
            if self.playing_board[0][0] == "O":
                print("You Lost...") 
                return True
        if self.playing_board[0][1] == self.playing_board[1][1] and self.playing_board[0][1] == self.playing_board[2][1]:
            if self.playing_board[0][1] == "X":
                print("You Won...")
                return True
            if self.playing_board[0][1] == "O":
                print("You Lost...") 
                return True
        if self.playing_board[0][2] == self.playing_board[1][2] and self.playing_board[0][2] == self.playing_board[2][2]:
            if self.playing_board[0][2] == "X":
                print("You Won...")
                return True
            if self.playing_board[0][2] == "O":
                print("You Lost...") 
                return True
        if len(self.available_spots) == 0:
            print("It's a Draw...")
            return True
        else:
            return False
                
play = TicTacToe()
  