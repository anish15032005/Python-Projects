#import modules
from machine_data import resources, menu, coins

machine_on = True
customer_money = 0
cash = 0
#prompt user by asking what would they like(espresso, latte, cappuccino), don't forget to run the loop so that it asks every time until the machine is turned off

while machine_on:
    user_input = input("What would you like?\n").lower()
    #turn off the machine by entering off to the prompt
    if user_input == "off":
        print("Machine is turned off")
        machine_on = False
    #print report
    elif user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n")
    elif user_input == "cash":
        print(f"Total cash: ${cash}")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        #process coins
        customer_money = quarters * coins["quarters"] + dimes * coins["dimes"] + nickels * coins["nickels"] + pennies * coins["pennies"]

    else:
        print("Invalid Input!!!")
        print("\n"*25)

        






    #check if the resources are sufficient or not
    if user_input == "espresso":
        if resources["water"] < menu["espresso"]["water"] or resources["coffee"] < menu["espresso"]["coffee"] or resources["milk"] < menu["espresso"]["milk"]: 
            print("Sorry resources is not enough to make espresso\nThe amount will be refunded")
        elif customer_money < menu["espresso"]["cost"]:
            print("Sorry the amount is not enough\nThe amount will be refunded")
        else:
            resources["water"] -= menu["espresso"]["water"]
            resources["milk"] -= menu["espresso"]["milk"]
            resources["coffee"] -= menu["espresso"]["coffee"]
            left_amount = customer_money - menu["espresso"]["cost"]
            cash += customer_money - left_amount
            
            
            print("Enjoy your espresso")
            print(f"Here is the change: ${left_amount}")
    if user_input == "latte":
        if resources["water"] < menu["latte"]["water"] or resources["coffee"] < menu["latte"]["coffee"] or resources["milk"] < menu["latte"]["milk"]: 
            print("Sorry resources is not enough to make latte\nThe amount will be refunded")
        elif customer_money < menu["latte"]["cost"]:
            print("Sorry the amount is not enough\nThe amount will be refunded")
        else:
            resources["water"] -= menu["latte"]["water"]
            resources["milk"] -= menu["latte"]["milk"]
            resources["coffee"] -= menu["latte"]["coffee"]
            left_amount = customer_money - menu["latte"]["cost"]
            cash += customer_money - left_amount
            print("Enjoy your latte")
            print(f"Here is the change: ${left_amount}")
    if user_input == "cappuccino":
        if resources["water"] < menu["cappuccino"]["water"] or resources["coffee"] < menu["cappuccino"]["coffee"] or resources["milk"] < menu["cappuccino"]["milk"]: 
            print("Sorry resources is not enough to make cappuccino\nThe amount will be refunded")
        elif customer_money < menu["cappuccino"]["cost"]:
            print("Sorry the amount is not enough\nThe amount will be refunded")
        else:
            resources["water"] -= menu["cappuccino"]["water"]
            resources["milk"] -= menu["cappuccino"]["milk"]
            resources["coffee"] -= menu["cappuccino"]["coffee"]
            left_amount = customer_money - menu["cappuccino"]["cost"]
            cash += customer_money - left_amount
            print("Enjoy your cappuccino")
            print(f"Here is the change: ${left_amount}")







    #check if the transaction is successful or not





    #make coffee


