import random
option = ["rock", "paper", "scissor"]
user = input('Enter user choice:')
system = random.choice(option)
print('My choice:',user)
print("System choice:", system)
if user == system:
    print("It's a tie!")

elif user == "rock" and system == "scissor":
    print("You win!")

elif user == "paper" and system == "rock":
    print("You win!")

elif user == "scissor" and system == "paper":
    print("You win!")
else:
    print("system wins!")