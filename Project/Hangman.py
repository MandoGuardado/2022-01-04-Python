from header import title
from words import game_words
from random import randint
from hangman_images import HANGMANPICS
import pandas as pd
from menus import main_menu, sub_menu, opening_menu
import os


# Initial function that get called to start the application
def start():
    # Greeting at the star of application
    print(title)
    input("Press enter to continue...\n")
    clear_console()
    csv_file = "user_data.csv"
    users_df = pd.read_csv(csv_file)
    response = login_user(users_df, main_menu, sub_menu)
    (player, validation) = response
    if validation:
        clear_console()
        print_welcome_title(player['user_name'])
        finish_playing = False
        total_player_score = int(player['score'])
        while not finish_playing:
            response = create_menu(opening_menu)
            if response == "1":
                total_player_score = play_game(total_player_score)
            elif response == "2":
                clear_console()
                print_dashboard(users_df)
            elif response == "3":
                finish_playing = True
            else:
                print("\n\nPlease select one of available options available.")
        clear_console()
        update_csv_file(users_df, player, total_player_score)
    else:
        print("\n\nIn order to play you must retrieve your old record or create a new one. Please come back soon ")
    print("\n\nSee you next time....")


# Function to update the .csv file - removes user record
def update_csv_file(df, user, current_score):
    user['score'] = current_score
    df = df.loc[df['user_name'] != user['user_name']]
    df.to_csv('user_data.csv', index=False)
    with open('user_data.csv', 'a') as fd:
        fd.write(f'\n{user["user_name"]},{user["name"]},{user["password"]},{str(user["score"])}')

    print("\n\nThanks for playing!\n\n")
    print("\n\nTake a look at the Scoreboard.\n\n")
    print(print_dashboard(pd.read_csv('user_data.csv')))


# Function to insert row into .csv with new user or updated score
def insert_row_csv_file(player):
    with open('user_data.csv', 'a') as fd:
        fd.write(f'\n{player["user_name"]},{player["name"]},{player["password"]},{player["score"]}')


# Function that prints out the Top 5 dashboard
def print_dashboard(d_frame):
    print("\n-----------------------------------------")
    print("     *     Hangman's TOP 5 Player    *     ")
    print("-----------------------------------------\n")
    print(pd.DataFrame(d_frame, columns=["user_name", "name", "score"]).sort_values(
        by="score", ascending=False).head(
        5).to_string(index=False))
    # print("\n\n")


# Function to create menu accepting a dict
def create_menu(menu):
    print("Please select from the following options:\n")
    for key in menu.keys():
        print(key, '--', menu[key])
    return input("\nEnter your choice: ").lower()


# Function to print the sub-menu banner
def print_submenu_title():
    print("\n-----------------------------------------")
    print("     ***      Submenu      ***           ")
    print("-----------------------------------------\n")


# Function to print the main menu banner
def print_main_menu_title():
    print("\n-----------------------------------------")
    print("     ***     Main Menu      ***          ")
    print("-----------------------------------------\n")


# Function to print a welcome banner
def print_welcome_title(name):
    print("\n-----------------------------------------")
    print(f"   *    Welcome {name}!      *       ")
    print("-----------------------------------------\n")


# function used to allow user to create new user or retrieve old record
def login_user(df, first_menu, second_menu):
    player = {}
    validated = False
    quit_program = False
    while not validated and not quit_program:
        print_main_menu_title()
        response = create_menu(first_menu)
        if response == "1":
            done_submenu = False
            while not done_submenu:
                print_submenu_title()
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


# function that clear the screen
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# function to prints header throughout the game
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


# Function that controls the flow of the game. Determine is letter needs to be displayed ,
# how lives left, and points accumulation (Accepts a user score)
def play_game(player_score: int):
    current_score = player_score
    clear_console()
    lives = len(HANGMANPICS) - 1  # uses the size of the hangman images list length to determine lives
    word = game_words[randint(0, len(game_words))]  # randomly selects a word form the list in words.py
    # print(word) #here for testing purposes
    display_placeholder = []  # starting empty list placeholder
    # for loops to apply '_'(underscore) as placeholder for each letter in word
    for x in word:
        display_placeholder.append("_")
    # boolean to determine when while loop below is done
    game_over = False
    # initial display banner
    game_display(lives, display_placeholder, current_score)
    # while loop that use game_over variable value to determine if player won or lost the game
    while not game_over:
        guess_letter = input("\n\tGuess a letter: ")
        clear_console()
        # If statement to determine if the guessed letter is in the random word and it has not been displayed
        if guess_letter in word and guess_letter not in display_placeholder:
            for x in range(len(word)):
                character = word[x]
                if character == guess_letter:
                    print("\nAwesome! guess letter is found.")
                    display_placeholder[x] = guess_letter
                    current_score += 10
            # if after found letter are displayed then it checks to see if there are any '_' (underscore)
            # left in display placeholder, if true then user winds game
            if "_" not in display_placeholder:
                clear_console()
                game_over = True
                print("\nAwesome you won!\n")
        # checks to see if letter is in random word but has already been displayed
        elif guess_letter in display_placeholder:
            print(f"\nYour already guessed the letter: {guess_letter}")
        # If statement when letter is not in word then user looses a live, points are lost, and checks
        # to see if you are out of lives
        if guess_letter not in word:
            clear_console()
            current_score -= 1
            lives -= 1
            print(f"\nGuess letter \'{guess_letter}\' is not in the word. You have {lives} lives left ")
            # Checks to see if user is out of lives, if true then user looses game
            if lives == 0:
                clear_console()
                current_score -= 10
                game_over = True
                print("\nYou lost this round")
        # displays updated banner
        game_display(lives, display_placeholder, current_score)
    return current_score


if __name__ == '__main__':
    start()
