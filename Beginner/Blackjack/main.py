from art import logo
from prompt import prompt_input
import validation as validator
from dealer import Dealer
from player import Player

############### Blackjack Project #####################

############### Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

computer = Dealer()
players = []

player_count = int(prompt_input("How many players? ", validator.is_number))
for player in range(player_count):
    name = prompt_input(
        f"Player {player + 1} enter name: ", validator.auto_valid)
    players.append(Player(name))


def run_game():
    print(f"{logo}")
    winners = []
    computer.deal_cards(players)

    for player in players:
        player.set_score()
        print(f"{player}'s hand: {player.hand} = {player.score}")

    print(f"{computer.name}'s hand: {computer.hand} = {computer.score}")
    if computer.score == 21:
        winners.append(computer.name)
    for player in players:
        if player.score == 21:
            winners.append(player)
    for player in players:
        while player.playing:
            if player.score < 21:
                if prompt_input(f"{player}'s score is now {player.score}, take another card? ", validator.yes_no) == 'y':
                    computer.hit(player)
                else:
                    player.hold()
            if player.score > 21:
                if validator.element_in(11, player.hand):
                    i = player.hand.index(11)
                    player.hand[i] = 1
                    player.set_score()
                else:
                    print(f"{player} is over 21")
                    player.bust()
        while computer.playing:
            while computer.score < 17:
                computer.hit(computer)
            if computer.score > 21:
                computer.bust()
            else:
                computer.hold()
    for player in players:
        if player.busted != True:
            if computer.busted == True:
                winners.append(player)
            elif computer.score < player.score:
                winners.append(player)
            elif computer.score == player.score:
                print(f"{computer} and {player} tied")
        else:
            winners.append(computer)
    print("Winners")
    for winner in winners:
        print(f"{winner}")
run_game()

##################### Hints #####################

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
