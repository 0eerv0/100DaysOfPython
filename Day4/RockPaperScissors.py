rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
bot = random.randint(0,2)
if answer >= 3 or answer < 0: 
  print("You typed an invalid number, you lose!") 
if answer == 0 and bot == 0:
  print(rock)
  print(f"Computer chose : {bot}")
  print(rock)
  print("Draw")
elif answer == 0 and bot == 1:
  print(rock)
  print(f"Computer chose : {bot}")
  print(paper)
  print("You Lose")
elif answer == 0 and bot == 2:
  print(rock)
  print(f"Computer chose : {bot}")
  print(scissors)
  print("You Win")

if answer == 1 and bot == 0:
  print(paper)
  print(f"Computer chose : {bot}")
  print(rock)
  print("You Win")  
elif answer == 1 and bot == 1:
  print(paper)
  print(f"Computer chose : {bot}")
  print(paper)
  print("Draw")
elif answer == 1 and bot == 2:
  print(paper)
  print(f"Computer chose : {bot}")
  print(scissors)
  print("You Lose")

if answer == 2 and bot == 0:
  print(scissors)
  print(f"Computer chose : {bot}")
  print(rock)
  print("You Lose")
elif answer == 2 and bot == 1:
  print(scissors)
  print(f"Computer chose : {bot}")
  print(paper)
  print("You Win")
elif answer == 2 and bot == 2:
  print(scissors)
  print(f"Computer chose : {bot}")
  print(scissors)
  print("Draw")


#Another Solution
'''game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")'''