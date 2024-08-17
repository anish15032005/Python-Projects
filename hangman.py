with open('words.txt','r') as file:
    word_list = [line.strip() for line in file]
#Choose a random word and assign it to the variable chosen_word.then print it

print('''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

import random
#create a variable called 'lives' to keep track of the lives left.
#set lives equal to 6
lives = 6

chosen_word =random.choice(word_list)


#Create a variable "placeholder" with the same number of "-" as the number of letters in the word.
placeholder = ""
for position in range(len(chosen_word)-1):
    placeholder += "-"
print(f"Word to guess: {placeholder}")

 
#Ask the user for a letter and store it in a variable guess. make guess lowercase
#Use a while loop to ask the user for guess again
game_over = False
correct_letters = []
while not game_over:
    print(f"******************{lives}/6 LIVES LEFT****************")
    guess = input("Guess a letter: ").lower()
    print(guess)
    
    #if the user has entered the letter which they have already guessed. let them know and print the letter
    print(f"You've already guessed {guess}") 

    display = ""

    #Check if guess is any of the letter in the chosen_word. print "Right" if it is, "Wrong" if it's not.
    #chanhge the for loop so that we can keep the guess in display
    for letter in chosen_word:
        
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            
        elif letter in correct_letters:
            display += letter
            
        
        else:
            display += "-"
    
    print(display)
    
    #if guess is not one of the letter in the chosen_word, Then reduce the lives by one.
    #if lives goes down to 0 then the game should stop and it should print "You lose."
    
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("********************YOU LOSE**********************")
            print(f"The word was {chosen_word}")
            game_over = True

    
    
    if "-" not in display:
        game_over = True
        print("**************YOU WIN*****************")
        
        
    #Print the ASCII art from 'stages'
    #that corresponds to current number of lives user has remaining
    print(stages[lives])
            
        
 