import random
from words import random_words


def get_name():
    """
    Asks user for their name to display
    Tell them the rules of the game
    """
    name = input("Hi! What's your name?\n")
    print(f"\nHi! {name}! Let's play hangman!\n")
    print("How to play:\n")
    print("The word is hidden under underscores.")
    print("A correct guess will reveal the letter.")
    print("You can guess letters or the whole word.")
    print("Each wrong guess you will lose you a life.")
    print("Each life lost will reveal part of the hangman.")
    print("You have 6 lives to guess the word or you lose.")
    print("Good luck!\n")


def play():
    """
    Check if the player wants to play the game
    """
    while True:
        user_input = input("\nWould you like to play? (Y/N):\n").upper()
        if user_input == "Y":
            print("\nGreat! Let's play!\n")
            return True
        elif user_input == "N":
            return False
        else:
            print("\nInvalid entry. Please enter 'Y' or 'N'.\n")


def generate_word():
    """
    Randomly select a word to use from the word list
    """
    random_word = random.choice(random_words)
    return random_word.upper()


def display_hangman(lives):
    """
    Create the hangman display in its different stages
    """
    if (lives == 5):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("=========\n")
    elif (lives == 4):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |    |  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("=========\n")
    elif (lives == 3):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |   /|  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("=========\n")
    elif (lives == 2):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |   /|\\")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("=========\n")
    elif (lives == 1):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |   /|\\")
        print(" |   /   ")
        print(" |       ")
        print(" |       ")
        print("=========\n")
    elif (lives == 0):
        print("---------")
        print(" |    |  ")
        print(" |    O  ")
        print(" |   /|\\")
        print(" |   / \ ")
        print(" |       ")
        print(" |       ")
        print("=========\n")


def play_game():
    """
    Call the play function to ask the user if they want to play or not.
    Display the word to the user.
    Allow the user to make guesses.
    Keep track of guessed letters and words so they can't be guessed again.
    Call the hang_man display function based on amount of lives lost.
    Determine if the user was correct or ran out of lives.
    """
    while True:
        play_the_game = play()

        if not play_the_game:
            print("\nOk, have a great day!\n")
            return

        guessed_letters = []
        guessed_words = []
        lives = 6
        game_over = False

        word = generate_word()
        print(word)
        hidden_word = "_ " * len(word)
        print(f"The word to guess is: {hidden_word}\n")

        while not game_over and lives > 0:
            print(f"letters guessed: ")
            for letter in guessed_letters:
                print(letter, end=" ")
            guess = input(f"\nPlease guess a letter or word:\n").upper()
            print(f"\nYou guessed: {guess}\n")
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print(f"You already guessed: {guess}!\n")
                elif guess not in word:
                    print(f"Sorry! {guess} is not in the word.\n")
                    lives -= 1
                    display_hangman(lives)
                    print(f"You lost a life, you have {lives} lives left.\n")
                    guessed_letters.append(guess)
                else:
                    print(f"Well done! {guess} is in the word!\n")
                    guessed_letters.append(guess)
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print(f"You already guessed: {guess}!\n")
                elif guess != word:
                    print(f"Sorry! {guess} is not the word!\n")
                    lives -= 1
                    display_hangman(lives)
                    print(f"You lost a life, you have {lives} lives left.\n")
                    guessed_words.append(guess)
                else:
                    game_over = True
            else:
                print("\nNot a valid Guess, please type a letter or word\n")
            display = ""
            for letter in word:
                if letter in guessed_letters:
                    display += letter + " "
                else:
                    display += "_ "
            if "_ " not in display:
                game_over = True
            print(f"The word to guess is: {display}\n")
        if game_over:
            print(f"You got it correct! The word was {word}\n")
        else:
            print(f"Sorry! You ran out of lives! The word was {word}\n")


def main():
    """
    Calls all the main functions to play the game.
    """
    get_name()
    word = generate_word()
    play_game()


main()
