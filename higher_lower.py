import random
print('''
       _     _ _____  ______ _     _ _______  ______     
 |_____|   |   |  ____ |_____| |______ |_____/     
 |     | __|__ |_____| |     | |______ |    \_     
                                                   
         _____  _  _  _ _______  ______            
 |      |     | |  |  | |______ |_____/            
 |_____ |_____| |__|__| |______ |    \_            
                                         ''')

print("Welcome to Higher Lower Game!")
people = {
    "Cristiano Ronaldo, A Footballer from Portugal": 647,
    "Lionel Messi, A Footballer from Argentina": 504,
    "Selena Gomez, A Singer and Actress from USA": 423,
    "Kylie Jenner, A Businesswoman from USA": 395,
    "Dwayne Johnson, An Actor from USA": 394,
    "Ariana Grande, A Singer from USA": 376,
    "Kim Kardashian, A Businesswoman from USA": 359,
    "Beyoncé, A Singer from USA": 313,
    "Khloé Kardashian, A Businesswoman from USA": 305,
    "Justin Bieber, A Singer from Canada": 295,
    "Zendaya, An Actress from USA": 180,
}

def higher_lower(user_ip, game_factor, points):
    points = 0
    while game_factor:
        random_peep1 = random.choice(list(people.items()))
        random_peep2 = random.choice(list(people.items()))
        
        # Ensure random_peep1 and random_peep2 are not the same
        while random_peep1 == random_peep2:
            random_peep2 = random.choice(list(people.items()))
        
        print(f"Who do you think has more Instagram followers?\nA. {random_peep1[0]}\nB. {random_peep2[0]}")
        user_ip = input("Type 'A' or 'B': ").upper()
        
        if user_ip == 'A' and random_peep1[1] > random_peep2[1]:
            print(f"Correct! {random_peep1[0]} has {random_peep1[1]}M followers.")
            points += 1
            game_factor = True
        elif user_ip == 'B' and random_peep2[1] > random_peep1[1]:
            print(f"Correct! {random_peep2[0]} has {random_peep2[1]}M followers.")
            points += 1
            game_factor = True
        elif user_ip not in ['A', 'B']:
            print("Invalid Input! Please enter 'A' or 'B'.")
            game_factor = True
        else:
            print("You got it wrong!")
            print(f"You got {points} points.")
            game_factor = False

higher_lower(user_ip='', game_factor=True, points=0)