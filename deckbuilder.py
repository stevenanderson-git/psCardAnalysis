import card
import random


class Deck:
    """Deck object that holds a list of cards
    deckname - string to name deck
    cardlist - list of Card objects
    totalcards - total number of cards initially in deck
    cardsremain - number of cards currently in deck
    """
    __slots__ = ['deckname', 'cardlist', 'totalcards', 'cardsremain']

    def __init__(self, deckname, cardlist):
        self.deckname = deckname
        self.cardlist = cardlist
        self.totalcards = len(cardlist)
        self.cardsremain = len(cardlist)

    def shuffle(self):
        """Shuffles the cards in the deck"""
        random.shuffle(self.cardlist)

    def draw(self, x):
        """Removes the first x elements of the deck and returns them in a list"""
        return [card for i in range (x)]