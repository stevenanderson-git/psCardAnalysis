from deckbuilder import Deck
from card import Card


def analyze_hand(hand):
    """Given a hand of MTG cards, will return a dictionary of how many of each card classification was in it."""
    hand_dict = {'threat': 0,'resource':0,'cardadvantage':0,'removal':0}
    for card in hand:
        if card.classification in hand_dict:
            hand_dict[card.classification] += 1
    
    return hand_dict

def analyze_multihand(deck, x, n):
    """Given a deck of MTG cards, it will run a Monte Carlo simulation
    to analyze x hands of n cards from the deck.
    Returns a list of hands which have been analyzed for threat, cardadvantage, resource, removal"""
    biglist = []
    deck.shuffle()
    for i in range(x):
        hand = deck.draw(n)
        biglist.append(analyze_hand(hand))
        deck.reset_deck(hand)
    return biglist