import random
# Dice game in Python

# Introduction and game rules.
print("""
When prompted, please type 1 if you are Player 1, 
or type 2 if you are Player 2

Goal: first to reach sum of 21 without going over.

First to the goal!  
Ernest Cline would be proud :-)

Good luck! 
""")

def play_game():
    sum = 0
    total_hold= 0
    while sum < 22:
        input("Please roll the die by hitting ENTER ... > ")
        roll = random.randint(1,6)
        print(f"You rolled a {roll}.")
        
        sum += roll
        print(f'Your total so far is: {sum}')

        hold = input("Press 'h' to hold or Enter to continue ... > ")
    
        if hold.lower() == 'h' and sum <= 21:
            total_hold = sum
            break
        
        if sum > 21:
            print("Woops. Sorry. Maybe next time.")
            break    
    return total_hold

#Select player
while True:
    player = (input("Which player are you? Choose 1 or 2 or other if done > "))

    if player == "1":
        total_one = play_game()
    elif player == "2":
        total_two = play_game()
    elif player !=1 or player !=2:
        break



if total_one <=21 and total_one>total_two:
    print("Player 1 wins")

elif total_two <=21 and total_two>total_one:
    print("Player 2 wins")

elif total_one == total_two:
    print("It's a tie!")







