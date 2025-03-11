name = input("enter your name")
price = int(input("enter your amount"))

bids = {}
bids[name] = price

def heighestBill(dict):
    winner = ""
    heighest_bid = 0
    for bidder in dict:
        amount = dict[bidder]
        if amount > heighest_bid:
            heighest_bid = amount
            winner = bidder
    print(f"the winner is {winner}")

continue_bidding = True
while continue_bidding:
    name = input("enter your name")
    price = int(input("enter your amount"))
    bids[name] = price
    should_continue = input("Do you have more participants? Type 'y' or 'n' ")
    if should_continue == 'n':
        heighestBill(bids)
    elif should_continue == 'y':
        print("\n"*20)




