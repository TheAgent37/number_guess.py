import random

MAX_GUESS = 3
MIN_NUM = 1
MAX_NUM = 5

print(
        f"""
Welcome to my number guessing game!


{'*'*60}
Rules:

-You have {MAX_GUESS} tries
-Random generated number is between {MIN_NUM} and {MAX_NUM} (both including)
-You can play the game how many as you want!
{'*'*60}

"""
    )

def guess():
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
            return try_again(True)

    print("You couldn't guess the number!\n\n")
    return try_again(True)


def try_again(win):
    if win:
        play = input("Congratulations! You wan't to play again? yes(y) no(n): ")
        print("\n")
        if play == "y":
            return guess()
        if play == "n":
            pass
        else:
            print("Invalid input")
            return try_again(win)
    else:
        play = input("Do you wan't to try again? yes(y) no(n): ")
        print("\n")
        if play == "y":
            return guess()
        if play == "n":
            pass
        else:
            print("Invalid input")
            return try_again(win)


guess()
