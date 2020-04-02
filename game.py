import random


def play(random_number):

    def helper(guess):
        guess = int(guess)
        if guess == random_number:
            print("That's correct.")
            return

        if guess > random_number:
            helper(input(f"{guess} is bigger. Guess something smaller: "))
        else:
            helper(input(f"{guess} is smaller. Guess something bigger: "))

    return helper(input('guess a number to match with computer: '))


play(random.randint(1, 100))

