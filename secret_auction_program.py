gavel = '''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                           
                       .-------------.
                      /_______________\ '''
                   
print(gavel)

ask = True

while ask :

    name = input("Enter Your name:\n")
    bid = int(input("Enter Your bid:\n$"))

    name_and_bids = {}

    name_and_bids[name] = bid
    bids = name_and_bids.values()
    maximum_bid = max(bids)
    maximum_bidder = ""
    for key,value in name_and_bids.items():
        if value == maximum_bid:
            maximum_bidder = key
    
    restart = input("Type Yes if you want to continue the bid else type No.\n").lower() 
    if restart == "no":
        ask = False
        print("\n"*100)
        print(f"The Winner of this bid is {maximum_bidder} with a bid of ${maximum_bid}.")
    elif restart == "yes":
        ask = True
        print("\n"*100)
    else:
        ask = False
        print("Error!!!\nInvalid Input")

  
    
