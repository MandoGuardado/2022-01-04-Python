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
import pandas as pd


# print(title)


def main():
    # name = input("What is your user name?: \n")
    csv_file = "user_data.csv"
    users_df = pd.read_csv(csv_file)
    dashboard = create_dashboard(users_df)
    print(dashboard)
    player = validate_user(users_df)
    print(player)

    # This is done at the end when player is done playing and they need to update their score
    # how to add a new user
    with open('user_data.csv', 'a') as fd:
        fd.write(f'\n{player["user_name"]},{player["name"]},{player["password"]},{player["score"]}')

    # print(player.name)
    # print(player.user_name)
    # result = users_df[users_df.user_name == "mando830"]
    # if result.empty:
    #     print("found it")
    # else:
    #     print("did not find record")
    # print("test")
    # print(result)
    # print(result.user_name == "mando830")
    # print("This is the Dashboard")


    # data_dict = users_df.to_dict()
    # print("This is the dict information")
    # print(data_dict)

    # Convert from dict to csv file
    # df = pd.DataFrame.from_dict(data_dict)
    # df.to_csv('test.csv', index=False, header=True)

    # print(users.sort_values(by="score", ascending=False))
    # print(f"What would you like to do {name}?: \n")

    # response = ''
    #
    # while response != "q":
    #     response = input("1: Stats *** 2: Play game **** q: to quit: \n")
    #     if response == "1":
    #         print("dashboard of winners ans score")
    #     elif response == "2":
    #         print("Playing game")
    #         # hangman_game()
    #     elif response == "q" or response =="Q":
    #         break
    #     else:
    #         print("You selected an option that is not available. ")
    # print(f"Thanks for playing {name}, see you next time!")


#     Update the scoreboard

def create_dashboard(d_frame):
    return pd.DataFrame(d_frame, columns=["user_name", "name", "score"]).sort_values(
        by="score", ascending=False).head(
        5).to_string(index=False)


def validate_user(df):
    player = {}
    validated = False
    while not validated:
        response = input(
            "Are you a returning player or new player, type in 'n' for new user or 'r' for returning").lower()
        if response == "r":
            response2 = input("Please type 'find' to find previous record or 'exit' to go to previous menu").lower()
            if response2 == "find":
                correct_user = False
                correct_password = False
                while not correct_user:
                    user_name = input("Please provide user name?\n")
                    if df[df.user_name == user_name].empty:
                        print("User name not found! Please try again\n")
                    else:
                        correct_user = True

                while not correct_password:
                    row = df[df.user_name == user_name]
                    password_input = input("Please enter password:\n")
                    password_bool = row.password.to_string(index=False) == password_input
                    if password_bool:
                        correct_password = True
                        player["user_name"] = row.user_name.to_string(index=False)
                        player["name"] = row.name.to_string(index=False)
                        player["password"] = row.password.to_string(index=False)
                        player["score"] = row.score.to_string(index=False)
                        validated = True

                    else:
                        print("That is the wrong password, Please try again!\n")

            else:
                continue

        elif response == "n":
            unique_name = False
            while not unique_name:
                user_name = input("Please select unique user name:\n")
                if df[df.user_name == user_name].empty:
                    unique_name = True
                    player["user_name"] = user_name
                    player["name"] = input("Type in name:\n")
                    player["password"] = input("Type in a password:\n")
                    player["score"] = 0
                    validated = True
    return player


def hangman_game():
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


main()
