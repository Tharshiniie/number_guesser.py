import random

top_of_range = input("Type a number to guess in that range of numbers: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()

else:
    print("Please type a number.")
    quit()

player_count = input("Number of players(max 4): ")

if player_count.isdigit():
    player_count = int(player_count)

    if player_count < 1 or player_count > 4:
        print("Number of players must be between 1 to 4.")
        quit()
else:
    print("Please enter a valid number of players.")
    quit()

players = []
for i in range(player_count):
    name = input(f"Enter name of player {i+1}: ")
    players.append(name)

print("Players:", players)

random_number = random.randint(0,top_of_range)

guesses_per_player = {player: 0 for player in players}

print(f"\n I have chosen a number between 0 and {top_of_range}. Let's start guessing!")

winner = None

while True:
    for player in players:
        guess= input(f"{player}, make a guess: ")

        if not guess.isdigit():
            print("Please type a number next time.")
            continue

        guess = int(guess)
        guesses_per_player[player] += 1

        if guess == random_number:
            print(f"{player} got it!")
            winner = player
            break
        elif guess > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")

    if winner:
        break
print(f"{player} got it in {guesses_per_player[player]} guesses!")
print(f"{player} is the winner!!")
