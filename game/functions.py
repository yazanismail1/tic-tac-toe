import os
import time
from game.classes import play

def playing():
    game_is_on = True
    print(play.__str__())
    print(play.board)
    user_input = input("Kindly choose a position.\n>> ")
    while game_is_on:
        if play.check_available_spots(user_input):
            play.update_playing_board_user(user_input)
            play.update_visual_board(user_input, "X") 
            print(play.board)
            os.system('clear')
            time.sleep(1)
            play.update_playing_board_bot()
            print(play.board)
            if play.check_winner():
                game_is_on = False
                return game_is_on
        user_input = input("Kindly choose a position.\n>> ")



            

