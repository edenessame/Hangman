import random
from words import random_words

def get_name():
    """
    Asks user for their name to display
    """
    name = input("What's your name?\n")
    print(f"Hi! {name}! Let's play hangman!\n") 

def generate_word():
    """
    Randomly select a word to use from a list 
    """
    pass

def hide_word():
    """
    Hide the word so it can't be seen
    """

def is_input_valid():
    """
    Check data input is valid
    Only allow letters and strings 
    Don't allow already guessed letters and string
    """
    pass

def play_game():
    """
    Allow the user to make guesses
    Keep track of guessed letters and words so they can't be guessed again
    Keep track of lives used
    """
    pass 

def display_hangman():
    """
    Create the hangman display in its different stages
    """
    pass

def main():
    """
    calls all the main functions
    """
    pass

get_name()