word = "smithers"
display = ["_", "_", "_", "_", "_", "_", "_", "_"]
lives = 10
wrongLetters = []
status = 0

print("""Welcome to Hangman! In this game you will have to figure out what the secret word is by guessing letters or guessing what the word could be.
      You will have 10 lives and each time you guess a wrong letter or your guessed word is wrong, you will lose a life. If you lose all of your lives, the game will end.
      Good Luck! 
      """)

def finishGame(Result):
    global status
    status = 1
    if Result == "Win":
        print("""Congratulations! You guessed the word. 
              Thanks for playing Hangman.""")
    elif Result == "Lose":
        print("You've run out of guesses. The word you were trying to get was: '", word, "'. Thanks for playing Hangman.")

def reveal_Letter(letter):
    score = 0
    for i in range(0, len(word)):
        if word[i] == letter:
            display[i] = letter
        if display[i] == word[i]:
            score += 1
    print(*display, sep="")
    if score == len(word):
        finishGame("Win")
    return

def check_guess(guess):
    if len(guess) > 1:
        if guess == word:
            finishGame("Win")
        else:
            lives -= 1
            if lives > 0:
                print("That word is incorrect, you have ", lives, " lives remaining.")
            else:
                finishGame("Lose")
    else:
        if guess in word:
            print("""The letter you guessed is correct and will now be added to the display
                  """)
            reveal_Letter(guess)

        else:
            lives -= 1
            if lives > 0:
                print("That letter is incorrect, you have ", lives, " lives remaining.")
                wrongLetters.append(guess)
                print("Wrong Letters: ", *wrongLetters, sep=", ")
            else:
                finishGame("Lose")

def guess():
    print("""To begin the game, Start by guessing a letter or word.
          """)
    while status != 1:
        while True:
            guess = input("Guess: ")
            return

        #check_guess(guess)
guess()

    
