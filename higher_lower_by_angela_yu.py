#import modules
#Generate a random account from the game data.
import random
from game_data import data

# Display art
logo = '''
  ___  ___  ___  ________  ___  ___  _______   ________          ___       ________  ___       __   _______   ________     
 |\  \|\  \|\  \|\   ____\|\  \|\  \|\  ___ \ |\   __  \        |\  \     |\   __  \|\  \     |\  \|\  ___ \ |\   __  \    
 \ \  \\\  \ \  \ \  \___|\ \  \\\  \ \   __/|\ \  \|\  \       \ \  \    \ \  \|\  \ \  \    \ \  \ \   __/|\ \  \|\  \   
  \ \   __  \ \  \ \  \  __\ \   __  \ \  \_|/_\ \   _  _\       \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \_|/_\ \   _  _\  
   \ \  \ \  \ \  \ \  \|\  \ \  \ \  \ \  \_|\ \ \  \\  \|       \ \  \____\ \  \\\  \ \  \|\__\_\  \ \  \_|\ \ \  \\  \| 
    \ \__\ \__\ \__\ \_______\ \__\ \__\ \_______\ \__\\ _\        \ \_______\ \_______\ \____________\ \_______\ \__\\ _\ 
     \|__|\|__|\|__|\|_______|\|__|\|__|\|_______|\|__|\|__|        \|_______|\|_______|\|____________|\|_______|\|__|\|__|
                                                                                                                           '''

print(logo)
    
def format_data(account):
    """Take the account data and convert it into printable format.""" 
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"   

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
        

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:


    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
        
    print(f"Compare A: {format_data(account_a)}")
    print('''                       
    .----.     .----.      
    \    \   /    /       
    '   '. /'   /        
    |    |'    /         
    |    ||    |    _    
    '.   `'   .'  .' |   
        \        /  .   | / 
        \      / .'.'| |// 
        '----'.'.'.-'  /  
                .'   \_.'   
                            ''')
    print(f"Compare B: {format_data(account_b)}")


        







    #Ask user for a guess.
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()
    #clear the screen
    print("\n"*20)
    print(logo)

    #Get follower count.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']


    #Use if statement to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)



    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Your current score is {score}.")
    else: 
        print(f"Sorry, that's wrong! Final score is {score}.")
        game_should_continue = False

#Score keeping.

#Make game repeatable.


#Making account at position B become the next account at position A.
