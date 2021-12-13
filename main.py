from analysis import analyze_multihand
from card import Card
from deckbuilder import Deck
import csv
import collections


def create_from_csv(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        cardlist = []
        # read each row
        for row in csvreader:
            # grab the data from the row
            quantity = int(row.pop(0))
            cardname = row.pop(0)
            supertype = row.pop(0)
            classification = str(row.pop(0))
            templist = []
            # make card objects for the quantity provided
            for i in range(quantity):
                if quantity > 1:
                    cid = i + 1
                else:
                    cid = 1
                templist.append(Card(cardname, supertype, cid, classification))
            # join the list of new cards with the decklist
            cardlist = cardlist + templist
        # build the deck
        deckname = filename.split('.', 1)[0]
        return Deck(deckname, cardlist)


def create_generic_deck(resources, threats, removal, cardadvantage):
    """Creates a generic deck of resources, threats, removal, and cardadvantage
    Cards created have a generic supertype, names are their classification with the count they were created on
    and only taged based on classification.
    """
    deckname = 'Generic Deck'
    cardlist = []
    for r in range(resources):
        cardlist.append(Card('RESOURCE_' + str(r), 'generic', r, 'resource'))
    for t in range(threats):
        cardlist.append(Card('THREAT_' + str(t), 'generic', t, 'threat'))
    for rem in range(removal):
        cardlist.append(Card('REMOVAL_' + str(rem), 'generic', rem, 'removal'))
    for ca in range(cardadvantage):
        cardlist.append(Card('CARDADVANTAGE_'+str(ca),
                        'generic', ca, 'cardadvantage'))
    return Deck(deckname, cardlist)


def begin_state(deck):
    """
    Generates a shuffled deck and hand of 7 cards and returns the objects.
    deck - a Deck of MTG cards
    """
    print("Shuffling")
    deck.shuffle()
    print(deck)
    print("Drawing 7")
    hand = deck.draw(7)
    print(deck)
    print('Cards in hand:')
    for c in hand:
        print(c)

    return deck, hand


# Beginning of analysis tests


def montehand_test_deck(deck, x):
    mh = analyze_multihand(deck, x, 7)
    counter = collections.Counter()
    for h in mh:
        counter.update(h)
    return dict(counter)
