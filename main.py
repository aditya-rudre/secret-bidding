from art import logo
import os
print(logo)
bids={}
def greatest_bidder(bidders_list):
    highest_bid=0
    winner = ""
    for bidder in bidders_list:
        bid_amount=bidders_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with the bid of ₹{highest_bid}.\nCongratulations to {winner}!!")

finished=False
while not finished:
    name=input("Enter your name : ")
    price=int(input("Enter your bid price : ₹"))
    bids[name]= price
    should_continue=input("Are there any other bidder? Types 'yes' or 'no' : ")
    if should_continue=="yes":
        os.system('clear')
    elif should_continue=="no":
        finished=True
        greatest_bidder(bids)
    




        
    
