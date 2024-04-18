![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

## Testing

* I commented out the code that hid the word so I could see what the word was to make sure the correct response was recieved. If the letter was in the word the message said that it was and what the letter entered was and if the letter wasn't in the word the message said it wasn't and what the letter entered was.
* I tested that it kept track of already guessed letters and words so they weren't guessed again. If a previously guessed letter or word was entered, the user was told they had already guessed that letter/word and didn't lose a life.
* I tested that the lives did decrease with each wrong guess and when they reached 0 the user was told they had lost. 

## Bugs

* The input didn't recognise uppercase guesses, so i had to add .upper to the word and the guess so that if either an upper or lowercase letter were guessed the program recognised them as the same.

## Credits

* Random words from [espressoenglish.net](https://www.espressoenglish.net/the-100-most-common-words-in-english/)