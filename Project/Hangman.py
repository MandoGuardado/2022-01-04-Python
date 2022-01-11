# Task 1:  Title is displayed - Completed
# Task 2:  Prompt user for name
#  Task 3:  Prompt user if they want to see Stats (read from file) or begin Playing, or quit
#  IF player opts to see stats, will access file and print details
# IF player opts  to quit, current score will be saved if higher than previous score
#  IF player opts to play
# generate workd and underscore values with image
# prompts user to letter or to solve
#           If user chooses letter:
#              If user guess right letter. then they are displayed with effect to handmand image
#               if user guess wrong letter, then hangman image changes
#             If user chooses to solve
#                 If guess is right then congratulating message
#                 if guess is wrong then hangman image changes

from header import title
from words import game_words
from random import randint

print(title)


def hangman_game():
    name = input("What is your user name?: \n")
    print(f"What would you like to do {name}?: \n")

    response = ''

    while response != "q":
        response = input("1: Stats *** 2: Play game **** q: to quit: \n")
        if response == "1":
            print("dashboard of winners ans score")
        elif response == "2":
            chances = 7
            word = game_words[randint(0, len(game_words))]
            print(word)
            display_word = []
            for x in word:
                display_word.append("_")

            game_over = False
            while not game_over:
                guess_letter = input("Guess a letter: ")
                if guess_letter in display_word:
                    print(f"Your already guessed this letter: {guess_letter}")
                for x in range(len(word)):
                    character = word[x]
                    if character == guess_letter:
                        display_word[x] = guess_letter
                print(' '.join(display_word))
                if guess_letter not in word:
                    chances -= 1
                    print(f"Guess letter is not in the word. You have {chances} chances left ")
                    if chances == 0:
                        game_over = True
                        print("You lost this round")
                if "_" not in display_word:
                    game_over = True
                    print("Awesome you won!")

            print("Playing game")

    print(f"Thanks for playing {name}, see you next time!")


#     Update the scoreboard


hangman_game()
