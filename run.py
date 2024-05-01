import random
from words import random_words

def get_name():
    """
    Asks user for their name to display
    """
    name = input("What's your name?\n")
    print(f"\nHi! {name}! Let's play hangman!\n") 

def generate_word():
    """
    Randomly select a word to use from the word list 
    Hide the word so it can't be seen
    """
    random_word = random.choice(random_words)
    #hidden_word = '_' * len(random_word)
    #print("The word is:\n")
    #print(hidden_word)
    return random_word.upper()


def is_input_valid():
    """
    Check data input is valid
    Only allow letters and strings 
    Don't allow already guessed letters and string
    """
    pass

#def hide_word(word):
    """
    When a letter is guessed correctly replace _ with the letter
    """
    #return ["_" for _ in word]

def display_hangman(lives):
    """
    Create the hangman display in its different stages
    """
    if (lives == 6):
    elif (lives == 5):
    elif (lives == 4):
    elif (lives == 3):
    elif (lives == 2):
    elif (lives == 1):

def play_game(word):
    """
    Allow the user to make guesses
    Keep track of guessed letters and words so they can't be guessed again
    Keep track of lives used
    """
    print(word) 
    #hidden_word = '_' * len(word)
    #print(hidden_word)
    print('_' * len(word))
    

    guessed_letters = []
    guessed_words = []
    lives = 6
    game_over = False    

    
    #display = " "
    while not game_over and lives > 0:
        print(f"letters guessed: ")
        for letter in guessed_letters:
            print(letter, end=" ")
        guess = input("\nPlease guess a letter or word: \n").upper()
        print(f"You guessed: {guess}")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed: {guess}!\n")
            elif guess not in word:
                print(f"Sorry! {guess} is not in the word.\n") 
                lives -= 1
                print(f"You lost a life, you have {lives} lives left.")
                guessed_letters.append(guess)   
            else:
                print(f"Well done! {guess} is in the word!\n")    
                guessed_letters.append(guess)
                display = ""
                for letter in word:
                    if letter in guessed_letters:
                        display += letter
                    else:
                        display += "_"
                if "_" not in display:
                        game_over = True    
                



                #for letter in word:
                    #if letter in guessed_letters:
                        #hidden_word = hidden_word.replace("_", letter)
                        #print(hidden_word)

        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in guessed_words:
                print(f"You already guessed: {guess}!\n")
            elif guess != word:
                print(f"Sorry! {guess} is not the word!\n")
                lives -= 1
                print(f"You lost a life, you have {lives} lives left.")
                guessed_words.append(guess)   
            else:
                game_over = True 
        else:
            print("\nNot a valid Guess, please try again\n") 
        print(display)    
        #print(f"\nThe word is: {hidden_word}")                        
    if game_over:
        print(f"\nCongratulations! You got the word was {word}\n")
    else:
        print(f"\nSorry! You ran out of lives! The word was {word}\n")     





def main():
    """
    calls all the main functions
    """
    pass

get_name()
word = generate_word()
play_game(word)