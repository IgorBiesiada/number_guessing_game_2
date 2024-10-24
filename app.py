def player_decision():
    # Predefined valid responses for the game.
    words = ['too small', 'too big', 'you win']

    # Loop until the user provides a valid response.
    while True:
        user_answer = input().lower()  # Get user input in lowercase.

        # Break the loop if the input is valid (i.e., in 'words').
        if user_answer in words:
            break

        # Notify the user if the input wasn't understood.
        print("Sorry, I didn't understand")

    return user_answer  # Return the valid response.


def program_guessed():
    print("Imagine a number between 0 and 1000!")
    print("Press 'Enter' to continue")

    input()  # Wait for the user to start the game.

    # Set the range for the guesses (1 to 1000).
    max_guess = 1000
    min_guess = 1
    user_answer = ""

    # Continue the guessing loop until the program wins ('you win').
    while user_answer != 'you win':
        # Calculate the middle of the current range for the guess.
        guess = int((max_guess - min_guess) / 2) + min_guess
        print(f'Is your number {guess}?')

        # Get the user's feedback on the guess.
        user_answer = player_decision()

        # Adjust the range based on the feedback ('too big' or 'too small').
        if user_answer == 'too big':
            max_guess = guess  # Narrow down the upper limit.
        elif user_answer == 'too small':
            min_guess = guess  # Narrow down the lower limit.

    print('I won hehe')  # Print victory message once guessed correctly.


# Main program entry point.
if __name__ == '__main__':
    program_guessed()  # Start the guessing game.