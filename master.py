import random


def get_user_input(options):
    return input("Type Rock/Paper/Scissors or Q to quit: ").lower()


def get_ai_choice(options):
    return random.choice(options)


def print_game_outcome(user_wins, ai_wins):
    print(f"You won {user_wins} times.")
    print(f"AI won {ai_wins} times.")
    print("Goodbye!")


def main():
    user_wins = 0
    ai_wins = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user_input = get_user_input(options)
        if user_input == "q":
            break
        if user_input not in options:
            print("Only rock, paper or scissors.")
            continue

        ai_pick = get_ai_choice(options)
        print(f"AI picked {ai_pick}.")

        if user_input == ai_pick:
            print("It's a draw!")
        elif (
            user_input == "rock"
            and ai_pick == "scissors"
            or user_input == "paper"
            and ai_pick == "rock"
            or user_input == "scissors"
            and ai_pick == "paper"
        ):
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            ai_wins += 1

    print_game_outcome(user_wins, ai_wins)


if __name__ == "__main__":
    main()
