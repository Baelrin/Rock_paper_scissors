import random

user_wins = 0
ai_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Only rock, paper or scissors.")
        continue

    # rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0, 2)
    ai_pick = options[random_number]
    print(f"AI picked {ai_pick}.")

    if (
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

print(f"You won {user_wins} times.")
print(f"AI won {ai_wins} times.")
print("Goodbye!")
