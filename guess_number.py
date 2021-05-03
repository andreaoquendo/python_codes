import random


def get_input():
    guess = input("Enter your guess: ")

    while check_user_input(guess) == False:
        print("You didn't choose a number.")
        guess = input("Enter your guess: ")
    return int(guess)


def check_user_input(i):
    try:
        i = int(i)
    except ValueError:
        return False


num = random.randint(0, 100)
score = 100
attempts = 1

guess = get_input()
while (guess == num) == False:
    if guess > num:
        print("your guess is higher than the actual number")
    else:
        print("your guess is lower than the actual number")
    score -= attempts*5
    if score < 0:
        break
    guess = get_input()

if score < 0:
    print("you lost!")
else:
    print("You won with " + str(score) + " points!")
