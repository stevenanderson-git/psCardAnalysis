import collections
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
        self.totalcards = len(self.cardlist)
        self.cardsremain = len(self.cardlist)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Deck: {}\ntotal cards: {}\ncards remain: {}".format(self.deckname, self.totalcards, self.cardsremain)
    
    def __iter__(self):
        return iter(self.cardlist)

    def shuffle(self):
        """Shuffles the cards in the deck"""
        random.shuffle(self.cardlist)

    def draw(self, x):
        """Removes the first x elements of the deck and returns them in a list"""
        temphand = [self.cardlist.pop(0) for i in range (x)]
        self.countcards()
        return temphand
    
    def reset_deck(self, hand):
        """Shuffles the hand back into the deck"""
        self.cardlist = self.cardlist + hand
        hand.clear()
        self.shuffle()
        self.countcards()
    
    def countcards(self):
        self.cardsremain = len(self.cardlist)
        return self.cardsremain

    def reset_draw7(self, hand):
        self.reset_deck(hand)
        return self.draw(7)

    def type_distribution(self):
        """Returns a dictionary that represents the total number of cards with each classification"""
        cdict = {'resource':0,'threat':0,'cardadvantage':0,'removal':0}
        for c in self.cardlist:
            cdict[c.classification] +=1
        return cdict