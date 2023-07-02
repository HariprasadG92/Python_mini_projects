import os
bids = {}
bidding_finshed = False

def highest_bidder(bid_rec):
    highest_bid = 0
    winner = ""
    
    for bidder in bid_rec:
        bid_amt = bid_rec[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner of the auction is {winner} with highest bid {highest_bid}")
        
while not bidding_finshed:
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    bids[name] = price
    conti = input("Are there any other bidder to continue? select: Yes or No \n").lower()
    
    if conti == "no":
        bidding_finshed = True
        highest_bidder(bids)
    elif conti == "yes":
        os.system('cls')