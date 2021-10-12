from os import system
from art import logo

clear = lambda:system('clear')

bidders = []

def show_logo():
    print(f"{logo}")

more_bidders = True
while more_bidders:
    name = input("What is your name? ")
    bid = input("Enter bid: ")
    bidders.append({'name': name, 'bid': float(bid)})
    yes_no = input("Are there more bidders?")
    if yes_no == 'no':
        more_bidders = False
    else:
        clear()
highest = {"name": 'none', 'bid': 0}
for bidder in bidders:
    if bidder['bid'] >= highest['bid']:
        highest = bidder

print(f"{highest['name']} wins with {highest['bid']}")