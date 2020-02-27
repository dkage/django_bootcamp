#####################################
#    WELCOME TO YOUR OOP PROJECT    #
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.deck = []
        self.split_a = []
        self.split_b = []
        self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        global SUITE, RANKS

        for suite_element in SUITE:
            for card_value in RANKS:
                card = [suite_element, card_value]
                self.deck.append(card)

    def shuffle_deck(self):
        shuffle(self.deck)

    def split_deck(self):
        deck_size = 52
        half = deck_size / 2
        self.split_a = []
        self.split_b = []

        for i in range(0, deck_size, 1):
            if i >= half:
                self.split_b.append(self.deck.pop())
            else:
                self.split_a.append(self.deck.pop())




class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """
    def __init__(self):
        self.cards_in_hand = []

    def remove_card(self):
        self.cards_in_hand.pop()

    def add_card(self, card_to_add):
        self.cards_in_hand.append(card_to_add)


class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self):
        super().__init__()
        self.name = ''

    def check_card_in_hand(self):
        if len(self.cards_in_hand) > 0:
            print('Cards in Hand')
            print(self.cards_in_hand)


######################
#      GAME PLAY     #
######################
print("Welcome to War, let's begin...")

current_deck = Deck()
current_deck.split_deck()

