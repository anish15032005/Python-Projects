import random
print("Welcome to the Random Password generator.")
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']

nr_letters = int(input("How many letters do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you like?\n"))
nr_numbers = int(input("How many numbers do you want?\n"))

random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
random_alphabets = [random.choice(alphabets) for _ in range(nr_letters-(nr_symbols+nr_numbers)) ]

random_symbols_str = "".join(random_symbols)
random_numbers_str = "".join(random_numbers)
random_alphabets_str = "".join(random_alphabets)

print("Your password is: "+random_alphabets_str+random_numbers_str+random_symbols_str)#It will print your password in an order like alphabet+numbers+symbols

strong_random_password_list = random_alphabets+random_symbols+random_numbers

strong_password = [random.choice(strong_random_password_list) for _ in range(nr_letters)]
strong_password_str = "".join(strong_password)
print(f"Your strong password is: {strong_password_str}")#I will recommend you to use this password as the order of alphabets,numbers and symbols are random
