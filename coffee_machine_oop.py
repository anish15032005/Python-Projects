from machine_data import resources, menu, coins

class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.menu = menu
        self.coins = coins
        self.cash = 0
        self.is_on = True

    def display_report(self):
        """Displays current resource levels and cash"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.cash}")

    def process_coins(self):
        """Collects and processes coins from the user"""
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        
        return (quarters * self.coins["quarters"] + 
                dimes * self.coins["dimes"] + 
                nickels * self.coins["nickels"] + 
                pennies * self.coins["pennies"])

    def check_resources(self, drink):
        """Checks if there are sufficient resources to make the drink"""
        for item, quantity in self.menu[drink].items():
            if item != "cost":
                if self.resources[item] < quantity:
                    print(f"Sorry, not enough {item} to make {drink}")
                    return False
        return True

    def make_drink(self, drink, payment):
        """Makes the drink and updates resources"""
        if payment < self.menu[drink]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            return False

        change = round(payment - self.menu[drink]["cost"], 2)
        self.cash += self.menu[drink]["cost"]

        # Update resources
        for item, quantity in self.menu[drink].items():
            if item != "cost":
                self.resources[item] -= quantity

        print(f"Here is ${change} in change.")
        print(f"Enjoy your {drink}! ☕")
        return True

    def process_order(self, choice):
        """Processes the complete drink order"""
        if self.check_resources(choice):
            payment = self.process_coins()
            self.make_drink(choice, payment)

    def run(self):
        """Main method to run the coffee machine"""
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            
            if choice == "off":
                print("Machine is turned off")
                self.is_on = False
            elif choice == "report":
                self.display_report()
            elif choice in self.menu:
                self.process_order(choice)
            else:
                print("\n" * 40)
                print("Invalid input")

def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.run()

if __name__ == "__main__":
    main()