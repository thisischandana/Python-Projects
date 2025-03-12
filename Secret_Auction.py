
def highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = " "
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bid:
            highest_bid == bidding_amount
            winner = bidder
    print(f"the winner is {winner}")







dict = {}
should_continue = True

while should_continue:
    names = input("Could you please enter your name?")
    bid_price = int(input("Could you please enter your price that you want to bid?"))
    ask = input("Is there any more bidders?'Y' or 'N")
#Add Name and bid into a dictionary as the key and value
    dict[names] = bid_price
    if ask == 'N':
        should_continue = False
        highest_bid(dict)

    else:
        print("Hey, Thanks for playing with us!")
        print("\n*20")

