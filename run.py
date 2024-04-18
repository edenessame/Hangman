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
    Randomly select a word to use from the word list 
    Hide the word so it can't be seen
    """
    word = random.choice(random_words)
    #hidden_word = '_' * len(word)
    print("The word is:\n")
    #print(hidden_word)
    #return(hidden_word)
    print(word)
    return word.upper()

def is_input_valid():
    """
    Check data input is valid
    Only allow letters and strings 
    Don't allow already guessed letters and string
    """
    pass

def play_game(word):
    """
    Allow the user to make guesses
    Keep track of guessed letters and words so they can't be guessed again
    Keep track of lives used
    """
    guessed_letters = []
    guessed_words = []
    lives = 6
    game_over = False

    while not game_over and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed: {guess}!")
            elif guess not in word:
                print(f"Sorry! {guess} is not in the word.") 
                lives -= 1
                guessed_letters.append(guess)   
            else:
                print(f"Well done! {guess} is in the word!")    
                guessed_letters.append(guess)
        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in guessed_words:
                print(f"You already guessed: {guess}!")
            elif guess != word:
                print(f"Sorry! {guess} is not the word!")
                lives -= 1
                guessed_words.append(guess)   
            else:
                game_over = True 
        else:
            print("Not a valid Guess, please try again")                     
    if game_over:
        print(f"congratulations! You got that {word} was the word")
    else:
        print(f"Sorry! You ran out of lives! The word was {word}")     


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
word = generate_word()
play_game(word)