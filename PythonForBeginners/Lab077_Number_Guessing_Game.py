import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is ?")

    while guess != secret_number:
        guess = int(input("Make a guess: "))

        if guess < secret_number:
            print("Your guess is too low.Try again ")
        elif guess > secret_number:
            print("Your guess is too high.Try again ")
        else:
            print("Congratulations, you guessed the number!")
number_guessing_game()