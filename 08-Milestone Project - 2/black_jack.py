import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self) -> str:
        deck_str = ""
        for card in self.all_cards:
            deck_str += '\n' + card.__str__()
        return deck_str

    def deal(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# Functions

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Your bet can't exceed {}".format(chips.total))
            else:
                break

def hit(hand, deck):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(hand, deck):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(hand, deck)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some_cards(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(dealer.cards[1])  

    # print("\nPlayer's Hand:")
    # for card in player.cards:
    #     print(card)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    
def show_all_cards(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand =",player.value)

# end of game
# check bust
def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")


# Game Logic
player_chips = Chips()

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Initialize deck, hand, chips
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chips)

    show_some_cards(player_hand, dealer_hand)
    
    # Player's turn
    while playing:
        hit_or_stand(player_hand,deck)
        show_some_cards(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break  

    # Dealer's turn
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(dealer_hand,deck)

        show_all_cards(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()        

    # Inform chips total
    print("\nPlayer's winnings stand at",player_chips.total)
    # Ask to play again  
    x = input('Do you want to play again? Enter y or n: ')

    if x[0].lower() == 'n':
        print('Thanks for playing.')
        break
    else:
        playing = True