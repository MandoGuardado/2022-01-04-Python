from header import title
from words import game_words
from random import randint
from hangman_images import HANGMANPICS
import pandas as pd
from menus import main_menu, sub_menu, opening_menu
import os


def start():
    # Greeting at the star of application
    print(title)
    input("Press enter to continue...\n")
    clear_console()
    csv_file = "user_data.csv"
    users_df = pd.read_csv(csv_file)
    response = validate_user(users_df, main_menu, sub_menu)
    (player, validation) = response
    if validation:
        clear_console()
        print_welcome_banner(player['user_name'])
        finish_playing = False
        total_player_score = int(player['score'])
        while not finish_playing:
            response = create_menu(opening_menu)
            if response == "1":
                total_player_score = hangman_game(total_player_score)
            elif response == "2":
                clear_console()
                print_dashboard(users_df)
            elif response == "3":
                finish_playing = True
            else:
                print("\n\nPlease select one of available options available.")
        clear_console()
        update_user_records(users_df, player, total_player_score)
    else:
        print("\n\nIn order to play you must retrieve your old record or create a new one. Please come back soon ")
    print("\n\nSee you next time....")


def update_user_records(df, user, current_score):
    if current_score > user['score']:
        user['score'] = current_score
        df = df.loc[df['user_name'] != user['user_name']]
        df.to_csv('user_data.csv', index=False)
        with open('user_data.csv', 'a') as fd:
            fd.write(f'\n{user["user_name"]},{user["name"]},{user["password"]},{str(user["score"])}')
    else:
        print("\n\nRecord was not update or created.")
    print("\n\nThanks for playing!\n\n")
    print("\n\nTake a look at the Scoreboard.\n\n")
    print(print_dashboard(pd.read_csv('user_data.csv')))


def update_player(player):
    with open('user_data.csv', 'a') as fd:
        fd.write(f'\n{player["user_name"]},{player["name"]},{player["password"]},{player["score"]}')


def print_dashboard(d_frame):
    print("\n-----------------------------------------")
    print("     *     Hangman's TOP 5 Player    *     ")
    print("-----------------------------------------\n")
    print(pd.DataFrame(d_frame, columns=["user_name", "name", "score"]).sort_values(
        by="score", ascending=False).head(
        5).to_string(index=False))
    print("\n\n")


def create_menu(menu):
    print("Please select from the following options:\n")
    for key in menu.keys():
        print(key, '--', menu[key])
    return input("\nEnter your choice: ").lower()


def print_main_menu_banner():
    print("\n-----------------------------------------")
    print("     ***     Main Menu      ***          ")
    print("-----------------------------------------\n")


def print_submenu_banner():
    print("\n-----------------------------------------")
    print("     ***      Submenu      ***           ")
    print("-----------------------------------------\n")


def print_welcome_banner(name):
    print("\n-----------------------------------------")
    print(f"   *    Welcome {name}!      *       ")
    print("-----------------------------------------\n")


def validate_user(df, first_menu, second_menu):
    player = {}
    validated = False
    quit_program = False
    while not validated and not quit_program:
        print_main_menu_banner()
        response = create_menu(first_menu)
        if response == "1":
            done_submenu = False
            while not done_submenu:
                print_submenu_options()
                response2 = create_menu(second_menu)
                if response2 == "1":
                    correct_user = False
                    correct_password = False
                    clear_console()
                    user_name = input("Please provide user name?\n")
                    if df[df.user_name == user_name].empty:
                        print("\nUser name not found! Please try again\n")
                    else:
                        correct_user = True
                    while not correct_password and correct_user:
                        row = df[df.user_name == user_name]
                        password_input = input("Please enter password:\n")
                        password_bool = row.password.to_string(index=False) == password_input
                        if password_bool:
                            clear_console()
                            correct_password = True
                            player["user_name"] = row.user_name.to_string(index=False)
                            player["name"] = row.name.to_string(index=False)
                            player["password"] = row.password.to_string(index=False)
                            player["score"] = int(row.score.to_string(index=False))
                            validated = True
                            done_submenu = True
                        else:
                            clear_console()
                            print(f"\nThat is the wrong password for user: {user_name}, Please try again!\n")
                elif response2 == "2":
                    done_submenu = True
                    clear_console()
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
            clear_console()
        else:
            print("The selection made is not available. Try Again!")
    return tuple((player, validated))


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def game_display(lives, display_word, player_score):
    print("\n-----------------------------------------")
    print(f"     ***      Hangman       ***           ")
    print("-----------------------------------------\n")
    print(f"           PlayerScore: {player_score}  \n")
    print("-----------------------------------------\n")
    print(HANGMANPICS[lives])
    print("\n\n")
    print("  Word: " + ' '.join(display_word) + "\n\n")
    print("\n-----------------------------------------\n")


def hangman_game(player_score):
    current_score = player_score
    clear_console()
    lives = len(HANGMANPICS) - 1
    word = game_words[randint(0, len(game_words))]
    print(word)
    display_word = []
    for x in word:
        display_word.append("_")
    game_over = False
    game_display(lives, display_word, current_score)
    while not game_over:
        guess_letter = input("\n\tGuess a letter: ")
        clear_console()
        if guess_letter in display_word:
            print(f"\nYour already guessed the letter: {guess_letter}")
        for x in range(len(word)):
            character = word[x]
            if character == guess_letter:
                print("\nAwesome! guess letter is found.")
                display_word[x] = guess_letter
                current_score += 10
        if guess_letter not in word:
            clear_console()
            current_score -= 1
            lives -= 1
            print(f"\nGuess letter \'{guess_letter}\' is not in the word. You have {lives} lives left ")
            if lives == 0:
                clear_console()
                current_score -= 10
                game_over = True
                print("\nYou lost this round")
        if "_" not in display_word:
            clear_console()
            game_over = True
            print("\nAwesome you won!\n")
        game_display(lives, display_word, current_score)
    return current_score


if __name__ == '__main__':
    start()
