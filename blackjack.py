print('''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |    
                              |____V|  ''') 

print(''' /$$       /$$                     /$$                               /$$      
| $$      | $$                    | $$                              | $$      
| $$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$__  $$| $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
| $$  \ $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ 
| $$  | $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/
                                       /$$  | $$                              
                                      |  $$$$$$/                              
                                       \______/  ''')     

print('''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |    
                              |____V|  ''') 


import random
#Rules of our Blackjack
#1. the deck is unlimited in size
#2. There are no jokers.
#3. The Jack/Queen/King all count as 10.
#4. The Ace can count 11 or 1.
#5. use the following list as the deck of cards:

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10 ] #For maintaining the case of probability we are counting 10 three times
comp_choice_1 = random.choice(cards)
comp_choice_2 = random.choice(cards)
comp_choice_3 = random.choice(cards)
comp_choice_4 = random.choice(cards)

ur_card_1 = random.choice(cards)
ur_card_2 = random.choice(cards)
ur_card_3 = random.choice(cards)
ur_card_4 = random.choice(cards)

comp_score1 = comp_choice_1 + comp_choice_2
comp_score2 = comp_score1 + comp_choice_3
comp_score3 = comp_score2 + comp_choice_4

ur_score1 = ur_card_1 + ur_card_2
ur_score2 = ur_score1 + ur_card_3
ur_score3 = ur_score2 + ur_card_4

game = True
while game:
    play = input("Press 'n' if you don't want to play the game else press any alphabetical letter.").lower()
    if play == 'n':
        print("Thank You")
        game = False
    print(f"The score of Your cards are {ur_card_1} and {ur_card_2}.\nPress 'h' if you want to HIT and press 's' if you you want to stand.").lower()



#The cards in the list have equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.
#The computer is the dealer
#The dealer will choose a maximum of 4 cards. so, the limitation of your cards is also 4

