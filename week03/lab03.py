import random


def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story.
    noun : str
        A noun to use in the story.
    verb : str
        A past-tense verb to use in the story.

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.
    """
    return (
        f"One day, a very {adjective} {noun} decided it was time to act, "
        f"so it bravely {verb} into the unknown and changed everything forever."
    )


def guessing_game():
    """
    Plays a number guessing game with the user.

    The user attempts to guess a randomly generated number between
    1 and 100, receiving feedback after each guess.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break


if __name__ == "__main__":
    guessing_game()
