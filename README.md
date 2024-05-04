# Hangman

Hangman is a word guessing game, where one person chooses a word and writes it down as a series of dashes representing the letters and another person tries to guess the word. 

If a letter is gessed correctly it is written in the place it should go in the word. 

If a guess is incorrect a part of a hanging man is drawn, with each wrong guess a different part of the body is drawn. 

The game ends when either the word is guessed correctly or the hanging man is completely drawn and the person has run out of guesses.

This is a computerized version, based inside a mock terminal deployed via Heroku, where the computer chooses the word and the user guesses it.

## Flow Chart

To understand how the logic of the game should work I created the following flow chart using Lucid Charts.
![Flow chart](README-assets/Hangman-Flowchart.png)

## Features



## Testing

* I commented out the code that hid the word so I could see what the word was to make sure the correct response was recieved. If the letter was in the word the message said that it was and what the letter entered was and if the letter wasn't in the word the message said it wasn't and what the letter entered was.
* I tested that it kept track of already guessed letters and words so they weren't guessed again. If a previously guessed letter or word was entered, the user was told they had already guessed that letter/word and didn't lose a life.
* I tested that the lives decreased with each wrong guess and when they reached 0 the user was told they had lost. 
* I tested as the lives decreased the different corresponding stages of the hangman image apeared and when it was complete the user was told they had run out of lives.

## Bugs

* The input didn't recognise uppercase guesses, so i had to add .upper to the word and the guess so that if either an upper or lowercase letter were guessed the program recognised them as the same.
* I was getting an error message for my word variable: "TypeError: argument of type 'builtin_function_or_method' is not iterable" one of the tutor team helped me realise that I was using the wrong syntax in my generate_word function: `return(word).upper` and I was returning the method of the string instead of an actual string, so I needed to change it to `return word.upper()`
* After each guess my display variable would save each iteration and append it next to the previous one and print the previous ones, rather than just the current guess, a member of the tutor team helped me realise that I needed to put the display variable inside the while loop so that it cleared each time and looked correct.


## Credits

* Help understanding and implementing Python came from the Code Institute course.

* Help in how to structure and layout a README file came from the Code Institutes [sample README](https://github.com/Code-Institute-Solutions/readme-template?tab=readme-ov-file)

* Random words from [espressoenglish.net](https://www.espressoenglish.net/the-100-most-common-words-in-english/)

* Inspirational support from [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w&t=292s)

* Further help and understanding was sought from [W3schools](https://www.w3schools.com/html/default.asp)

* The Code Institute tutor support team for helping guide me.

* My mentor, Medale Oluwafemi, for his invaluable knowledge and guidance.

Welcome eden essame,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.