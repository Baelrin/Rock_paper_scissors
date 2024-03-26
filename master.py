import enum
import random
from typing import List, Optional


class Choice(enum.Enum):
    ROCK = "rock"  # Represents the rock choice in the game
    PAPER = "paper"  # Represents the paper choice in the game
    SCISSORS = "scissors"  # Represents the scissors choice in the game


# Defines winning conditions for each choice
WIN_CONDITIONS: dict[Choice, List[Choice]] = {
    Choice.ROCK: [Choice.SCISSORS],  # Rock beats scissors
    Choice.PAPER: [Choice.ROCK],  # Paper beats rock
    Choice.SCISSORS: [Choice.PAPER],  # Scissors beats paper
}


def get_user_input(options: List[Choice]) -> Optional[Choice]:
    """Prompt the user for a choice among the given options.

    Args:
        options: A list of Choice enum members representing valid game options.

    Returns:
        A Choice enum member representing the user's input or None if the
        user chooses to quit the game.
    """
    choices_str = ", ".join([option.value for option in options])
    user_input = input(f"Type {choices_str} or Q to quit: ").lower()
    if user_input == "q":
        return None
    try:
        return Choice(user_input)
    except ValueError:
        print(
            f"Invalid choice '{user_input}'. Please enter one of the following: {choices_str}."
        )
        return get_user_input(options)


def get_ai_choice(options: List[Choice]) -> Choice:
    """Select a choice randomly for the AI from the given options.

    Args:
        options: A list of Choice enum members representing valid game options.

    Returns:
        A Choice enum member representing the AI's choice.
    """
    return random.choice(options)


def determine_winner(user_choice: Choice, ai_choice: Choice) -> str:
    """Determine the winner of a game round.

    Args:
        user_choice: The Choice enum member representing the user's selection.
        ai_choice: The Choice enum member representing the AI's selection.

    Returns:
        A string indicating the winner: 'user', 'ai', or 'draw'.
    """
    if user_choice == ai_choice:
        return "draw"
    elif ai_choice in WIN_CONDITIONS[user_choice]:
        return "user"
    else:
        return "ai"


def print_game_outcome(user_wins: int, ai_wins: int, draws: int) -> None:
    """Print the outcome of the game including the number of wins and draws.

    Args:
        user_wins: The number of rounds won by the user.
        ai_wins: The number of rounds won by the AI.
        draws: The number of rounds that ended in a draw.
    """
    print(f"You won {user_wins} times.")
    print(f"AI won {ai_wins} times.")
    print(f"There were {draws} draws.")
    print("Goodbye!")


def main() -> None:
    """Main function to execute the Rock, Paper, Scissors game logic."""
    user_wins = 0
    ai_wins = 0
    draws = 0
    options = list(Choice)

    print("Welcome to Rock, Paper, Scissors! Let's play.")

    while True:
        user_choice = get_user_input(options)
        if user_choice is None:  # User chose to quit
            break

        ai_choice = get_ai_choice(options)
        print(f"AI picked {ai_choice.value}.")

        winner = determine_winner(user_choice, ai_choice)
        if winner == "draw":
            print("It's a draw!")
            draws += 1
        elif winner == "user":
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            ai_wins += 1

    print_game_outcome(user_wins, ai_wins, draws)


if __name__ == "__main__":
    main()
