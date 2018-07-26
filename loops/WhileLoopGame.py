import random

n = 10
to_be_guessed = int(random.random() * n) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Guess the number(1 to 10): "))
    if guess > 0:
        if guess < to_be_guessed:
            print("Number is too small")
        elif guess > to_be_guessed:
            print("Number is too large")
    else:
        print("Sorry! that you are giving up")
        break

else:
    print("Congratulations! You made it...")
