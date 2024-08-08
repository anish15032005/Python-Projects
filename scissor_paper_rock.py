import random


print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
print("Welcome to the game.")
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
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
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
choices = [scissor,paper,rock]

ur_choice = input('Enter your choice "scissor","paper" or "rock".\n').lower()

if ur_choice == "scissor":
    print(scissor)
elif ur_choice == "paper":
    print(paper)
elif ur_choice == "rock":
    print(rock)
else:
    print("Your choice is invalid.")


    

computer_choice = random.choice(choices)

print(computer_choice)

if ur_choice == "scissor" and computer_choice == rock:
    print("You lost!!")
    
if ur_choice == "scissor" and computer_choice == paper:
    print("You Won!!")
    
if ur_choice == "scissor" and computer_choice == scissor:
    print("Draw!!")
    
if ur_choice == "paper" and computer_choice == paper:
    print("Draw!!")
    
if ur_choice == "paper" and computer_choice == scissor:
    print("You lost!!")
    
if ur_choice == "paper" and computer_choice == rock:
    print("You won!!")
    
if ur_choice == "rock" and computer_choice == rock:
    print("Draw!!")
    
if ur_choice == "rock" and computer_choice == scissor:
    print("You lost!!")
    
if ur_choice == "paper" and computer_choice == rock:
    print("You Won!!")

    
    