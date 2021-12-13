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

def analysis_test_100(x):
    d100 = create_from_csv('100_test2.csv')
    mh = analyze_multihand(d100, x, 7)
    counter = collections.Counter()
    for hand in mh:
        counter.update(hand)    
    return dict(counter)


def begin_state(filename):
    """
    Generates a shuffled deck and hand of 7 cards and returns the objects.
    filename - a string representation of a deck in .csv form
    """
    print("Building Deck")
    deck = create_from_csv(filename)
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


def test_60_1():
    return begin_state('60_test1.csv')

def test_60_2():
    return begin_state('60_test2.csv')

def test_100_1():
    return begin_state('100_test1.csv')

def test_100_2():
    return begin_state('100_test2.csv')