import random

hand_dict = {1: '✊',
             2: '✋', 
             3: '✌️'}

print("""
===================
Rock Paper Scissors
===================
1) ✊
2) ✋
3) ✌️
""")

player = int(input("Pick a number: "))
computer = random.randint(1, 3)

print(f"You chose: {hand_dict[player]}\nCPU chose: {hand_dict[computer]}")

if computer == 1 and player == 2:
    print("The player won!")
elif computer == 1 and player == 3:
    print("The CPU won!")
elif computer == 2 and player == 1:
    print("The CPU won!")
elif computer == 2 and player == 3:
    print("The player won!")
elif computer == 3 and player == 1:
    print("The player won!")
elif computer == 3 and player == 2:
    print("The CPU won!")
else:
    print("Its a Tie!")