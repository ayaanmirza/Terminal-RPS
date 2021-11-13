import random

# Bot Choice
int_choice = random.randint(1,3)
if int_choice == 1:
     bot_choice = "rock"
elif int_choice == 2:
    bot_choice = "paper"
elif int_choice == 3:
    bot_choice = "scissors"

user_score = 0
bot_score = 0

print("The score is:", user_score, "/", bot_score)

# User Input
user_input = input("rock, paper, or scissors: ")

# A lot of if statements T^T
if user_input == bot_choice:
    print("Tie! You both chose " + bot_choice)
    print("The score is the still the same: ", user_score, "/", bot_score)
# Rock vs Scissors
elif user_input == "rock" and bot_choice == "scissors":
    print("You win! You chose rock and the bot chose scissors")
    user_score += 1
    print("The score is:", user_score, "/", bot_score)
elif user_input == "scissors" and bot_choice == "rock":
    print("You lose! You chose scissors and the bot chose rock")
    bot_score += 1
    print("The score is:", user_score, "/", bot_score)
# Rock vs Paper
elif user_input == "rock" and bot_choice == "paper":
    print("You lose! You chose rock and the bot chose paper")
    bot_score += 1
    print("The score is:", user_score, "/", bot_score)
elif user_input == "paper" and bot_choice == "rock":
    print("You win! You chose paper and the bot chose rock")
    user_score += 1
    print("The score is:", user_score, "/", bot_score)
# Scissors vs Paper
elif user_input == "scissors" and bot_choice == "paper":
    print("You win! You chose scissors and the bot chose paper")
    user_score += 1
    print("The score is:", user_score, "/", bot_score)
elif user_input == "paper" and bot_choice == "scissors":
    print("You lose! You chose paper and the bot chose scissors")
    bot_score += 1
    print("The score is:", user_score, "/", bot_score)

# Do you want to play again?
rematch = input("Do you want to play again? (y/n): ")


# Repeats code above untill user enters n
while rematch == 'y':
        # Bot Choice
    int_choice = random.randint(1,3)
    if int_choice == 1:
        bot_choice = "rock"
    elif int_choice == 2:
        bot_choice = "paper"
    elif int_choice == 3:
        bot_choice = "scissors"
    print("The score is:", user_score, "/", bot_score)

    # User Input
    user_input = input("rock, paper, or scissors: ")

    # A lot of if statements T^T
    if user_input == bot_choice:
        print("Tie! You both chose " + bot_choice)
        print("The score is the still the same: ", user_score, "/", bot_score)
    # Rock vs Scissors
    elif user_input == "rock" and bot_choice == "scissors":
        print("You win! You chose rock and the bot chose scissors")
        user_score += 1
        print("The score is:", user_score, "/", bot_score)
    elif user_input == "scissors" and bot_choice == "rock":
        print("You lose! You chose scissors and the bot chose rock")
        bot_score += 1
        print("The score is:", user_score, "/", bot_score)
    # Rock vs Paper
    elif user_input == "rock" and bot_choice == "paper":
        print("You lose! You chose rock and the bot chose paper")
        bot_score += 1
        print("The score is:", user_score, "/", bot_score)
    elif user_input == "paper" and bot_choice == "rock":
        print("You win! You chose paper and the bot chose rock")
        user_score += 1
        print("The score is:", user_score, "/", bot_score)
    # Scissors vs Paper
    elif user_input == "scissors" and bot_choice == "paper":
        print("You win! You chose scissors and the bot chose paper")
        user_score += 1
        print("The score is:", user_score, "/", bot_score)
    elif user_input == "paper" and bot_choice == "scissors":
        print("You lose! You chose paper and the bot chose scissors")
        bot_score += 1
        print("The score is:", user_score, "/", bot_score)
    
    # Do you want to play again?
    rematch = input("Do you want to play again? (y/n): ")


print("Okay, the game has ended.")

# Prints final score based on condition
if user_score == bot_score:
    print("Tie! You both had a score of", user_score)
elif user_score > bot_score:
    print("You win! You had a final score of", user_score)
elif user_score < bot_score:
    print("Sorry, you lost. The bot had a score of", bot_score)