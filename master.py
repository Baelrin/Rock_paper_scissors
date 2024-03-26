import random
import enum


# Define an enumeration for the choices to improve clarity and prevent errors
class Choice(enum.Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


# Function to get the user's input and validate it
def get_user_input(options):
    choices = ", ".join([option.value for option in options])
    return input(f"Type {choices} or Q to quit: ").lower()


# Function to get the AI's choice
def get_ai_choice(options):
    return random.choice(options)


# Function to determine the winner of the round
def determine_winner(user_choice, ai_choice):
    win_conditions = {
        Choice.ROCK: [Choice.SCISSORS],
        Choice.PAPER: [Choice.ROCK],
        Choice.SCISSORS: [Choice.PAPER],
    }
    if user_choice == ai_choice:
        return None
    elif ai_choice in win_conditions[user_choice]:
        return "User"
    else:
        return "AI"


# Function to print the outcome of the game
def print_game_outcome(user_wins, ai_wins, draws):
    print(f"You won {user_wins} times.")
    print(f"AI won {ai_wins} times.")
    print(f"There were {draws} draws.")
    print("Goodbye!")


def main():
    user_wins = 0
    ai_wins = 0
    draws = 0
    options = list(Choice)

    print("Welcome to Rock, Paper, Scissors! Let's play.")

    while True:
        user_input = get_user_input(options)
        if user_input == "q":
            break
        try:
            user_choice = Choice(user_input)
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        ai_choice = get_ai_choice(options).value
        print(f"AI picked {ai_choice}.")

        winner = determine_winner(user_choice, ai_choice)
        if winner is None:
            print("It's a draw!")
            draws += 1
        elif winner == "User":
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            ai_wins += 1

    print_game_outcome(user_wins, ai_wins, draws)


if __name__ == "__main__":
    main()
