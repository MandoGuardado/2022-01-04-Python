from header import title
from words import game_words
from random import randint
import pandas as pd
from menus import main_menu, sub_menu, opening_menu
import os


def main():
    # Greeting at the star of application
    print(title)
    input("Press enter to continue...\n")
    clear_console()
    csv_file = "user_data.csv"
    users_df = pd.read_csv(csv_file)
    dashboard = create_dashboard(users_df)
    response = validate_user(users_df, main_menu, sub_menu)
    (player, validation) = response
    if validation:
        finish_playing = False
        total_player_score = int(player['score'])
        while not finish_playing:
            response = print_menu(opening_menu)
            if response == "1":
                total_player_score += hangman_game(total_player_score)
            elif response == "2":
                print(dashboard)
            elif response == "3":
                finish_playing = True
            else:
                print("Please select one of options available.")
        player['score'] = total_player_score
        # TODO Save score into user_data.csv with update score (using method)
    else:
        print("In order to play you must retrieve your old record or create a new one. Please come back soon ")

    print(player)
    print("See you next time....")


def update_player(player):
    with open('user_data.csv', 'a') as fd:
        fd.write(f'\n{player["user_name"]},{player["name"]},{player["password"]},{player["score"]}')


def create_dashboard(d_frame):
    return pd.DataFrame(d_frame, columns=["user_name", "name", "score"]).sort_values(
        by="score", ascending=False).head(
        5).to_string(index=False)


def print_menu(menu):
    print("Please select from the following options:")
    for key in menu.keys():
        print(key, '--', menu[key])
    return input("Enter your choice: ").lower()


def print_mainmenu():
    print("-----------------------------------------")
    print("     ***     Main Menu      ***          ")
    print("-----------------------------------------")


def print_submenu():
    print("-----------------------------------------")
    print("     ***      Submenu      ***           ")
    print("-----------------------------------------")


def validate_user(df, first_menu, second_menu):
    player = {}
    validated = False
    quit_program = False
    while not validated and not quit_program:
        print_mainmenu()
        response = print_menu(first_menu)
        if response == "1":
            done_submenu = False
            while not done_submenu:
                response2 = print_menu(second_menu)
                if response2 == "1":
                    correct_user = False
                    correct_password = False
                    user_name = input("Please provide user name?\n")
                    if df[df.user_name == user_name].empty:
                        print("User name not found! Please try again\n")
                    else:
                        correct_user = True
                    while not correct_password and correct_user:
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
                            done_submenu = True
                        else:
                            print("That is the wrong password, Please try again!\n")
                elif response2 == "2":
                    done_submenu = True
                else:
                    print("The selection made is not available. Try Again")
        elif response == "2":
            unique_name = False
            user_name = input("Please select unique user name:\n")
            while not unique_name:
                if df[df.user_name == user_name].empty:
                    unique_name = True
                    player["user_name"] = user_name
                    player["name"] = input("Type in name:\n")
                    player["password"] = input("Type in a password:\n")
                    player["score"] = 0
                    validated = True
                else:
                    user_name = input("User name is already taken, please try again:\n")
        elif response == "3":
            quit_program = True
        else:
            print("The selection made is not available. Try Again!")
    return tuple((player, validated))


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def hangman_game(player_score):
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
                player_score += 5
        print(' '.join(display_word))
        if guess_letter not in word:
            player_score -= 1
            chances -= 1
            print(f"Guess letter is not in the word. You have {chances} chances left ")
            if chances == 0:
                player_score -= 10
                game_over = True
                print("You lost this round")
        if "_" not in display_word:
            game_over = True
            print("Awesome you won!")
    return player_score


main()
