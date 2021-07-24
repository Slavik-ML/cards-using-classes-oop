import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.as_array = [self.suit, self.value]

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for number in range(2, 15):
                card = Card(suit, number)
                self.deck.append(card.as_array)

    def show_each_card_of_deck(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            new_position = random.randint(0, i)
            self.deck[i], self.deck[new_position] = self.deck[new_position], self.deck[i]

    def drawCard(self):
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def pick_card(self, deck):
        new_card = deck.drawCard()
        self.hand.append(new_card)

    def show_hand(self):
        for card in self.hand:
            print(card)

    def discard(self):
        return self.hand.pop()