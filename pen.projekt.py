import random

stats = {
    "games_played": 0,
    "player_wins": 0,
    "computer_wins": 0
}

def greet():
    print("Welcome to the Soccer Penalty Shootout!")

def get_direction(prompt):
    directions = ["left", "center", "right"]

    while True:
        choice = input(prompt).lower().strip()

        if choice in directions:
            return choice

        print("Please type left, center or right.")

def show_stats():
    print("\n--- STATISTICS ---")
    print("Games played:", stats["games_played"])
    print("Player wins:", stats["player_wins"])
    print("Computer wins:", stats["computer_wins"])

def take_penalties(player_score, computer_score, round_name):
    directions = ["left", "center", "right"]

    print("\n" + round_name + ":")

    player_scored = False
    computer_scored = False

    player_shot = get_direction("Choose your shot direction (left, center, right): ")
    computer_guess = random.choice(directions)

    if player_shot == computer_guess:
        print("Goalkeeper guessed " + computer_guess + "! Shot saved!")
    else:
        print("Goalkeeper guessed " + computer_guess + ". Goal!")
        player_score += 1
        player_scored = True

    computer_shot = random.choice(directions)
    player_guess = get_direction("Guess the computer's shot direction (left, center, right): ")

    if computer_shot == player_guess:
        print("You guessed " + player_guess + "! You saved it!")
    else:
        print("Computer shot " + computer_shot + ". Goal for computer!")
        computer_score += 1
        computer_scored = True

    print("Score: You " + str(player_score) + " - " + str(computer_score) + " Computer")

    return player_score, computer_score, player_scored, computer_scored

def penalty_shootout():
    player_score = 0
    computer_score = 0
    rounds = 5

    for i in range(rounds):
        player_score, computer_score, player_scored, computer_scored = take_penalties(
            player_score,
            computer_score,
            "Round " + str(i + 1)
        )

    extra_round = 1

    while player_score == computer_score:
        player_score, computer_score, player_scored, computer_scored = take_penalties(
            player_score,
            computer_score,
            "Sudden Death Round " + str(extra_round)
        )

        if player_scored != computer_scored:
            break

        extra_round += 1

    print("\nFinal Score:")
    print("You " + str(player_score) + " - " + str(computer_score) + " Computer")

    stats["games_played"] += 1

    if player_score > computer_score:
        print("You win!")
        stats["player_wins"] += 1
    else:
        print("Computer wins!")
        stats["computer_wins"] += 1

def menu():
    greet()

    while True:
        print("\n--- MENU ---")
        print("1. Play game")
        print("2. Show stats")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            penalty_shootout()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

menu()