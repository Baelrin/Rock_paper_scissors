import random


def get_ai_choice(options):
    return random.choice(options)


def determine_winner(user_choice, ai_choice, win_conditions):
    if user_choice == ai_choice:
        return None
    elif ai_choice in win_conditions[user_choice]:
        return "user"
    else:
        return "ai"


def main():
    user_wins = 0
    ai_wins = 0
    options = ["rock", "paper", "scissors"]
    win_conditions = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break
        if user_input not in options:
            print("Only rock, paper, or scissors.")
            continue

        ai_pick = get_ai_choice(options)
        print(f"AI picked {ai_pick}.")

        winner = determine_winner(user_input, ai_pick, win_conditions)
        if winner == "user":
            print("You won!")
            user_wins += 1
        elif winner == "ai":
            print("You lost!")
            ai_wins += 1
        else:
            print("It's a draw!")

    print(f"You won {user_wins} times.")
    print(f"AI won {ai_wins} times.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
