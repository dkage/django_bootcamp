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
import sys

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
        self.player_deck = []

    def check_card_in_hand(self):
        if len(self.cards_in_hand) > 0:
            print('Cards in Hand')
            print(self.cards_in_hand)


def deck_add(cards_to_add, deck):
    if len(cards_to_add) == tuple:
        deck.insert(0, cards_to_add)
    elif len(cards_to_add) > 1:
        print('pool')

    return 1


def who_wins():
    global player_card, cpu_card, player, cpu

    winner = 'TBD'
    if value_of_card(player_card) > value_of_card(cpu_card):
        print("Human Player Won! Card pool going to Human deck")
        deck_add(player_card, player.player_deck.pop())
        deck_add(cpu_card, player.player_deck.pop())
        winner = 'Human'

    elif value_of_card(cpu_card) > value_of_card(player_card):
        print("CPU Won this round! Card pool going to CPU deck.")
        deck_add(player_card, cpu.player_deck.pop())
        deck_add(cpu_card, cpu.player_deck.pop())
        winner = 'CPU'

    else:
        input("It's a DRAW, War starts!")
        war()
        # TODO add pool

    return winner


def war():
    global player, cpu, player_card, cpu_card

    war_pool.append(player_card)
    war_pool.append(cpu_card)
    for n in range(0, 2, 1):
        war_pool.append(player.player_deck.pop())
        war_pool.append(cpu.player_deck.pop())
    player_card = player.card_deck.pop()
    cpu_card = cpu.card_deck.pop()

    wins = who_wins()
    if wins == "Human":
        player.player_deck = war_pool + player.player_deck
        print("Human wins war. Pool added to his deck.")
    elif wins == 'CPU':
        cpu.player_deck = war_pool + cpu.player_deck
        print("CPU wins war. Pool added to it's deck.")

    return True


def value_of_card(card_to_evaluate):
    global RANKS

    card_num_letter = card_to_evaluate[1]
    return RANKS.index(card_num_letter)


######################
#      GAME PLAY     #
######################
print("Welcome to War, let's begin...")

# Generate decks and split them
current_deck = Deck()
current_deck.split_deck()

# Instance players and
cpu = Player()
player = Player()

cpu.player_deck = current_deck.split_a
player.player_deck = current_deck.split_b

num_round = 0
war_pool = []

print("Game starts!")

while len(player.player_deck) > 0 and len(cpu.player_deck) > 0:
    print("============================================================")
    print("============================================================")
    input("\n\nPress Enter to play round...\n\n")

    player_card = player.player_deck.pop()
    cpu_card = cpu.player_deck.pop()

    print("DRAWING PHASE: \n")
    print("Human Player draw: {}".format(player_card))
    print("CPU draw card: {}".format(cpu_card))
    print("\n")
    who_wins()

    # print("Starting new round: \n\n\n")
    # num_round = num_round + 1
    # print("Number of cards in each deck:\n")
    # print("Player Human: {}\n".format(len(player.player_deck)))
    # print("Player CPU: {}\n".format(len(cpu.player_deck)))
    #
    # input("\n\nPress Enter to play round...\n\n")
    #
    # player_card = player.player_deck.pop()
    # cpu_card = cpu.player_deck.pop()
    #
    # print("Player Human: {}\n".format(len(player.player_deck)))
    # print("Player CPU: {}\n".format(len(cpu.player_deck)))
    #
    # print("Cards drawn\n")
    # print("Player Human Card: {}\n".format(player_card))
    # print("Player Human RANK: {}, value {}\n\n".format(player_card[1], RANKS.index(player_card[1])))
    # print("Player CPU Card: {}".format(cpu_card))
    # print("Player cpu RANK: {}, value {}\n\n".format(cpu_card[1], RANKS.index(cpu_card[1])))
    #
    # input("\n\nPress Enter...\n\n")
    #
    # if RANKS.index(player_card[1]) > RANKS.index(cpu_card[1]):
    #     print("Player card is higher, human player won!\n")
    #
    #     player.player_deck.insert(0, player_card)
    #     player.player_deck.insert(0, cpu_card)
    #
    #     input("\n\nPress Enter to continue...\n\n")
    #
    # elif RANKS.index(cpu_card[1]) > RANKS.index(player_card[1]):
    #     print("CPU card is higher, human player won!\n")
    #
    #     cpu.player_deck.insert(0, cpu_card)
    #     cpu.player_deck.insert(0, player_card)
    #
    #     input("\n\nPress Enter to continue...\n\n")
    #
    # else:
    #     print("DRAW, STARTING WAR!\n\n\n")
    #     print("Putting cards in pool.")
    #
    #     war_pool.append(player_card)
    #     war_pool.append(cpu_card)
    #
    #     for i in range(0, 2, 1):
    #         war_pool.append(player.player_deck.pop())
    #         war_pool.append(cpu.player_deck.pop())
    #
    #     print("War card pool follows:\n")
    #     print(war_pool)
    #
    #     input("\n\nPress Enter to Battle...\n\n")
    #
    #     if RANKS.index(player_card[1]) > RANKS.index(cpu_card[1]):
    #         print("Player card is higher, human player won!\n")
    #
    #         player.player_deck.insert(0, player_card)
    #         player.player_deck.insert(0, cpu_card)
    #
    #         for war_card in war_pool:
    #             player.player_deck.insert(0, war_pool.pop())
    #
    #         input("\n\nPress Enter to continue...\n\n")
    #
    #     elif RANKS.index(cpu_card[1]) > RANKS.index(player_card[1]):
    #         print("CPU card is higher, human player won!\n")
    #
    #         cpu.player_deck.insert(0, cpu_card)
    #         cpu.player_deck.insert(0, player_card)
    #
    #         for war_card in war_pool:
    #             cpu.player_deck.insert(0, war_pool.pop())
    #
    #         input("\n\nPress Enter to continue...\n\n")

        # TODO put validations in function for recursion in case double Wars

# TODO add more messages telling who won, and better comment each round
if len(player.player_deck) == 0:
    print("Human Player Lost, CPU WON!")
elif len(cpu.player_deck) == 0:
    print("Human Player Lost, CPU WON!")



