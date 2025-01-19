import random

# Constants for the number of turns for each difficulty level
easy_level_turns = 10
hard_level_turns = 5

def game():
    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a random number between 1 and 100
    answer = random.randint(1, 100)

    # Function to set the difficulty level
    def set_difficulty():
        # Ask the user to choose a difficulty level
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        # Return the number of turns based on the chosen difficulty
        if level == "easy":
            return easy_level_turns
        else:
            return hard_level_turns

    # Set the number of turns based on the chosen difficulty
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    # Initialize guess variable
    guess = 0

    # Loop until the user guesses the correct number or runs out of turns
    while guess != answer and turns > 0:
        # Ask the user to make a guess
        guess = int(input("Make a guess: "))
        # Decrease the number of turns by 1
        turns -= 1
        # Check the user's guess against the answer
        check_answer(guess, answer)
        # If the guess is incorrect, inform the user of the remaining attempts
        if guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")

    # If the user guessed the correct number, print a success message
    if guess == answer:
        print("You got it! The answer was", answer)
    # If the user ran out of turns, print a failure message
    else:
        print("You've run out of guesses, you lose. The number was", answer)

# Function to check the user's guess against the answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("Correct!")

# Start the game
game()