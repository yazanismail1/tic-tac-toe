import pytest
from game.classes import TicTacToe

@pytest.fixture
def user_instance():
    user = TicTacToe()
    return user


# @pytest.mark.skip("todo")
def test_classes_str(user_instance):
    welcome_message = """
      W  |  E  |  L 
    -----------------
      C  |  O  |  M 
    -----------------
      E  |  .  |  . 
    
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

    """
    assert user_instance.__str__() == welcome_message

# @pytest.mark.skip("todo")
def test_board(user_instance):
    board = """
      1  |  2  |  3 
    -----------------
      4  |  5  |  6 
    -----------------
      7  |  8  |  9 
    """

    assert user_instance.board() == board

# @pytest.mark.skip("todo")
def test_available_spot(user_instance):
    availables = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert user_instance.available_spots == availables

# @pytest.mark.skip("todo")
def test_check_available_spots(user_instance):
    position = 3

    assert user_instance.check_available_spots(position) == True

# @pytest.mark.skip("todo")
def test_check_turns(user_instance):
    assert user_instance.check_turns() == "user"