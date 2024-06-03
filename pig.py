import random

def roll (): # this is to get the random number for the dice
    
    min_num = 1
    max_num = 6

    roll = random.randint(min_num, max_num)
    return roll


while True: #this is to get the number of players

    players = input ("Enter the number of players (2 - 4): ")
    if players.isdigit(): #check if the input is a digit
        players = int(players) #convert the input to an integer
        if 2 <= players <= 4: #check if the input is within the range
            break #exit the loop
        else:   #if the input is not within the range
            print ("Please enter a number between 1 and 4")     #print an error message

print ("The number of players are: ", players)

max_score = 100
players_scores = [0 for _ in range(players)] #this creates a list of zeros for each player

print ("The scores are: ", players_scores)

while max(players_scores) < max_score:
    current_score = 0 

    print ("Player 1: ", players_scores[0])
    print ("Player 2: ", players_scores[1])

    should_continue = input ("Do you want to roll the dice (y)?: ")
    if should_continue.lower() != "y":
         break
    else:
        value = roll()
    if value == 1:
        print ("You rolled a 1. You lose all of  your points")
    else:
        current_score += value
        print ("You rolled a: ", value)


   
   

