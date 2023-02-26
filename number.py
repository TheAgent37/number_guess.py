import random

MAX_GUESS = 3
MIN_NUM = 1
MAX_NUM = 5

print(
    f"""
Welcome to my number guessing game!
        

{"*"*60}
Rules:

-You have {MAX_GUESS} tries
-Random generated number is between {MIN_NUM} and {MAX_NUM} (both including)
-You can play the game how many as you want!
{"*"*60} 

"""
)


def Guess():
    guess_count = int()
    num = random.randint(MIN_NUM, MAX_NUM)
    print(f"Random number created between {MIN_NUM} and {MAX_NUM}\n")
    while guess_count < MAX_GUESS:
        gnum = input(f"You have {MAX_GUESS-guess_count} tries left. Enter your guess: ")
        try:
            int(gnum)
        except ValueError:
            print("Error! Please enter a number.\n\n")
            continue
        gnum = int(gnum)
        guess_count += 1

        if gnum > num:
            print("Your guess is too high.\n")

        if gnum < num:
            print("Your guess is too low.\n")

        if gnum == num:
            print(f"You guess the number ({num}) in {guess_count} tries!\n\n")
            Try_again(True)
    else:
        print("You couldn't guess the number!\n\n")
        Try_again(False)


def Try_again(win):
    while win:
        play = input("Congratulations! You wan't to play again? yes(y) no(n): ")
        print("\n")
        if play == "y":
            Guess()
        if play == "n":
            exit()
        else:
            print("Invalid input")
            Try_again(win)
    while win is False:
        play = input("Do you wan't to try again? yes(y) no(n): ")
        print("\n")
        if play == "y":
            Guess()
        if play == "n":
            exit()
        else:
            print("Invalid input")
            Try_again(win)


Guess()
