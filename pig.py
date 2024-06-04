import random

# This is a simple game called Pig

def roll():
    # This is to get the random number for the dice
    min_num = 1
    max_num = 6

    roll = random.randint(min_num, max_num)
    return roll


while True:
    # This is to get the number of players
    players = input("Enter the number of players (2 - 4): ")
    # Ask the user to enter the number of players

    if players.isdigit():
        # Check if the input is a digit
        players = int(players)
        # Convert the input to an integer

        if 2 <= players <= 4:
            # Check if the input is within the range
            break
            # Exit the loop
        else:
            # If the input is not within the range
            print("Please enter a number between 1 and 4")
            # Print an error message

print("The number of players are: ", players)

# def randomPlayer():
#     # this is to pick a random player to start the game
#     min_num = 1
#     max_num = 4

#     roll = random.randint(min_num, max_num)
#     return roll

max_score = 30
# This is the maximum score that a player can reach to win the game
players_scores = [0 for _ in range(players)]
# This creates a list of zeros for each player

print("The scores are: ", players_scores)

while max(players_scores) < max_score:

    for player_index in range(players):
    
        print("\n Player ", player_index + 1, " your turn to play! \n")
        print("\n your total score is: ", players_scores[player_index], "\n")
        current_score = 0
        
        while True:
            should_continue = input("Do you want to roll the dice (y)?: ")
            if should_continue.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1. You lose all of your points")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
                print("Your current score is: ", current_score)

        players_scores[player_index] += current_score
        print("The scores are: ", players_scores[player_index])

max_score = max(players_scores) # This is to get the maximum score among the players

winning_index = players_scores.index(max_score) # This is to get the index of the player with the maximum score. it is the maximum score at the index of the player

print("The winner is player ", winning_index + 1) # This is to print the winner of the game


 

   


   
   

