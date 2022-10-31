import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def split_half(self):
        first_half = self.all_cards[:26]
        second_half = self.all_cards[26:]
        return (first_half, second_half)
    # def deal_one(self):
    #     return self.all_cards.pop()


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    def add_card(self, card):
        if type(card) == type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)

    def remove_card(self):
        return self.all_cards.pop(0)

    def __str__(self) -> str:
        return f'{self.name} has {len(self.all_cards)} cards'


# Game Logic

# Initialize
p1 = Player("Player one")
p2 = Player("Player two")

complete_cards = Deck()
complete_cards.shuffle()


first_half, second_half = complete_cards.split_half()
p1.add_card(first_half)
p2.add_card(second_half)

# for i in range(0, len(first_half)):
#     print(first_half[i].value)

game_on = True

round_count = 0


while game_on:
    round_count += 1
    print(f'Round {round_count}')
    # check if any player is out of cards
    if len(p1.all_cards) == 0:
        print(f'{p1.name} out of cards. loses')
        game_on = False
        break
    if len(p2.all_cards) == 0:
        print(f'{p2.name} out of cards. loses')
        game_on = False
        break

    p1_on_hold_cards = []
    p2_on_hold_cards = []

    curr_card_p1 = p1.remove_card()
    curr_card_p2 = p2.remove_card()

    p1_on_hold_cards.append(curr_card_p1)
    p2_on_hold_cards.append(curr_card_p2)

    # type(p1_on_hold_cards)

    at_war = True

    while at_war:

        if p1_on_hold_cards[-1].value > p2_on_hold_cards[-1].value:
            p1.add_card(p1_on_hold_cards)
            p1.add_card(p2_on_hold_cards)
            # break
            at_war = False
        elif p1_on_hold_cards[-1].value < p2_on_hold_cards[-1].value:
            p2.add_card(p1_on_hold_cards)
            p2.add_card(p2_on_hold_cards)
            # break
            at_war = False
        else:
            print('WAR!')
            if len(p1.all_cards) < 5:
                print(f'{p1.name} run out of cards at war. Lose')
                game_on = False
                break
            elif len(p2.all_cards) < 5:
                print(f'{p2.name} run out of cards at war. Lose')
                game_on = False
                break
            else:
                for i in range(5):
                    p1_on_hold_cards.append(p1.remove_card())
                    p2_on_hold_cards.append(p2.remove_card())


# if __name__ == '__main__':
#     game_play()
