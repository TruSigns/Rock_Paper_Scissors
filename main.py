import random
# This will generate a random number.
# randomNum = random.randint(1, 1000)
# random_float = random.random()
# print(random_float)
# print(randomNum)

# stringNames = input("Give me everybody's names, separated by a comma. ")
# splitNames = stringNames.split(",")
# chosenName = random.randint(0, 2)
# print(f"{splitNames[chosenName]} is going to buy the meal today!")

# dirty_dozen =["strawberry", "banana", "apples", "oranges"]
# dirty_craps = ["chicken", "eggs", "steaks"]
# dirty_combines = [dirty_craps, dirty_craps]
# print(dirty_combines)

# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# hori = int(position[0])
# vert = int(position[1])
#
# sr =  map[vert-1]
# sr[hori-1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

import random

print("Welcome to Rock, Paper, Scissor games")

# Paper(0) beats Rocks(1)
# Rocks(1) beats Scissors(2)
# Scissors(2) beats Paper(0)

# Player and Computer choice
p1_choice = int(input("What are you going to choose: 0.Paper 1.Rock 2.Scissors"))
cpu_choice = random.randint(0,2)

if p1_choice == 0 and cpu_choice == 1:
    print("Player Wins; paper beats rocks")
elif cpu_choice == 0 and p1_choice == 1:
    print("You Lose; paper beats rocks")
elif p1_choice == cpu_choice:
    print("Draw!!!")
elif p1_choice >= 3 or p1_choice <= 0:
    print("Invalid entry")
elif cpu_choice > p1_choice:
    print("Computer wins")
elif p1_choice > cpu_choice:
    print("You Win!")






# Printing computer choice
print(f"The computer has chosen: {cpu_choice}")

