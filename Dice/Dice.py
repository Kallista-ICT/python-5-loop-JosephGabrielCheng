import random

# Showing variables (score and rolls)
score = 0
rolls = []

# Welcoming the player and explaining on how to play the game
name = input("Hello what is your name? ")
print(f" Hello {name}!!, welcome to the Dice game")
print("The game is very simple!")
print("To win the game, you should roll a dice!")
print("When  you roll a die, you will recieve a random number, which is your point!")
print("You should atleast reach 50 points to win!")

# Dice will keep on rolling and will give number 1 to 6 until the total score is more than 50 or 50
while score < 50:
    input("Please click enter to roll the dice")
    die = random.randint (1,6)
    score += die # The score will be added to the amount rolled in the die
    rolls.append(die) # Adding the result of die to a list

    print(f"You have rolled {die} points!!")
    print(f"Your total score now is {score}")


# Congratulating the player and showing the total of their score and the list of their rolls
print("Congratulation!! you have won the game!!")
print(f"You have rolled {score} amount of scores!!")
print("This are the rolls that you had rolled")
print(f"\nALL roll: , {rolls}")