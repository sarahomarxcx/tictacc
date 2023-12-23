"""
Tic Tac Toe game
"""

from time import sleep
import random


class Player:
    """
    A class used to represent a Player
    """

    def __init__(self, name, symbol):
        """
        Class constructor
        :param name: player name
        :param symbol: player symbol
        """
        self.name = name
        self.symbol = symbol


class TicTacToe:
    """
    A class used to represent a Tic Tac Toe game
    """
    # Constants
    EMPTY_BOARD = """
-------------
 {} | {} | {}
-------------
 {} | {} | {}
-------------
 {} | {} | {}
-------------
"""
    EMPTY_SYMBOL = "  "

    def __init__(self, players):
        """
        Class constructor
        :param players: list of players
        """
        # Attributes
        # List of pieces in the board, starts with empty pieces
        self.pieces = [self.EMPTY_SYMBOL] * 9
        # Winner symbol of the game
        self.winner = None
        # List of players
        self.players = players

    def move(self, player: Player, move):
        """
        Makes a move in the board, if the move is valid
        :param player: Player that is making the move
        :param move: Move to be made
        :return: True if the move was made, False otherwise
        """
        # Check if the move is valid and if the cell is empty
        if self.is_empty(move) and move in range(9):
            # Make the move
            self.pieces[move] = player.symbol
            return True
        # If the move is not valid, return False
        return False

    def get_board(self):
        """
        Returns the board in a string format with the pieces in it
        :return: Board in a string format
        """
        # Format the board with the pieces
        return self.EMPTY_BOARD.format(*self.pieces)

    def is_empty(self, move):
        """

        :param move:
        :return:
        """
        return self.pieces[move] == self.EMPTY_SYMBOL

    def get_empty_cells(self):
        """
        Returns a list of empty cells in the board
        :return:
        """
        return [i for i, piece in enumerate(self.pieces)
                if piece == self.EMPTY_SYMBOL]

    def is_over(self):
        """
        Checks if the game is over and sets the winner
        :return: None
        """

        game_over = False
        # Check rows and columns for a winner
        for i in range(3):
            if self.pieces[i * 3] == self.pieces[i * 3 + 1]\
                    == self.pieces[i * 3 + 2] != self.EMPTY_SYMBOL:
                self.winner = self.pieces[i * 3]
                game_over = True
            if self.pieces[i] == self.pieces[i + 3] == self.pieces[i + 6] != self.EMPTY_SYMBOL:
                self.winner = self.pieces[i]
                game_over = True

        # Check diagonals for a winner
        if self.pieces[0] == self.pieces[4] == self.pieces[8] != self.EMPTY_SYMBOL:
            self.winner = self.pieces[0]
            game_over = True
        if self.pieces[2] == self.pieces[4] == self.pieces[6] != self.EMPTY_SYMBOL:
            self.winner = self.pieces[2]
            game_over = True

        # If there are no empty cells, the game is over
        if len(self.get_empty_cells()) == 0:
            return True
        # Return the game over flag
        return game_over

    def get_winner(self):
        """
        Returns name of the winner of the game
        :return: Name of the winner
        """
        # Check who is the winner
        for player in self.players:
            if player.symbol == self.winner:
                return player.name
        return None

def get_player_move(player, game):
    """
    Gets a move from the player and makes it
    :param player: The player
    :param game: The game
    :return: None
    """
    # Loop until the player makes a valid move
    while True:
        # Get the move from the player
        move = input("Choose a move [1-9]: ")
        # Try to make the move and break the loop if it's valid
        try:
            # Subtract 1 from the move because the board starts at 1
            move = int(move) - 1
            # Check if the move is valid
            if game.move(player, move):
                break
            # If the move is not valid, print an error message
            print("Come on! Choose a valid move!")
            continue
        # If the move is not a number, print an error message
        except ValueError:
            print("That's not even a number!")
            continue


def play_computer_move(computer, game):
    """
    Makes a move for the computer
    :param computer: The computer player
    :param game: The game
    :return: None
    """
    # Get a random empty cell
    move = random.choice(game.get_empty_cells())
    # Make the move
    game.move(computer, move)


def play_game():
    """
    Plays a game of Tic Tac Toe
    :return:
    """
    # List of phrases that the computer will say
    computer_phrases = [
        "Such a bad move! I'm gonna win!",
        "You're so bad at this!",
        "Is this your first time playing?",
        "I can't believe you're doing this!",
        "I don't even know why I'm playing with you!",
        "My grandma could do better than this!",
        "I'm gonna win this game!",
        "I don't even have an AI and I'm still winning!",
        "You should give up!",
        "Why are you even trying?",
        "What's the point of playing if you're gonna lose anyway?",
        "Really? What's your IQ?"
    ]
    # Shuffle the phrases, so they are said in a random order
    random.shuffle(computer_phrases)
    # Create a new game
    game = TicTacToe([user_player, computer_player])
    # Print an initial empty board
    print(game.get_board())

    print("I dare you to a Tic Tac Toe game!")
    print("You're playing against a computer, so you're gonna lose anyway!")
    # Play the game until it's over
    while True:
        # Get player move
        get_player_move(user_player, game)
        # Print the board
        print(game.get_board())
        sleep(1)
        # Check if the game is over
        if game.is_over():
            break

        print(computer_phrases.pop())
        # Play computer move
        play_computer_move(computer_player, game)
        # Print the board
        print(game.get_board())
        sleep(1)
        # Check if the game is over
        if game.is_over():
            break
    # Print the winner
    print("Game over!")
    winner = game.get_winner()
    if winner is None:
        print("It's a tie!")
    else:
        print(f"{game.get_winner()} won!")


# Create the player and the computer
player_name = input("What's your name? ")
print(f"Hello, {player_name}!")
user_player = Player(player_name, "❌")
computer_player = Player("I", "⭕")
# Play the game until the player doesn't want to play again
while True:
    # Play the game
    play_game()
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? [y/n] ")
    if play_again.lower() != "y":
        break
# Print a goodbye message
print("See you later!")
