from art import logo
from replit import clear
print(logo)

def winner_bid(bids):
    highest_bid = 0
    for person in bids:
        if bids[person] > highest_bid:
            highest_bid = bids[person]
            winner = person
    return winner, highest_bid

bids = {}

status = True
while status:
    bidder = input("What's your name?:")
    price = int(input("What is your bid?: $"))
    bids[bidder] = price
    check = input("Are there any other bidders? Type 'yes' or 'no'.")
    if check == 'no':
        status = False
        winner, bid = winner_bid(bids)
        print(f'The winner is {winner} with a bid of ${bid}.')
    elif check == 'yes':
        clear()