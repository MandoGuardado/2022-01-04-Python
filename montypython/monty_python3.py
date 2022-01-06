#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian" and answer != "Shrubbery":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")

    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

