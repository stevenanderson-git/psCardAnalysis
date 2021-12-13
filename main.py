from card import Card
from deckbuilder import Deck
import csv




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
            classification = row
            templist = []
            # make card objects for the quantity provided
            for i in range(quantity):
                if quantity > 1:
                    cid = i + 1
                else:
                    cid = 1
                templist.append(Card(cardname, supertype, cid, classification=classification))
            # join the list of new cards with the decklist
            cardlist = cardlist + templist
        # build the deck
        deckname = filename.split('.', 1)[0]
        return Deck(deckname, cardlist)

def test_60_1():
    print("Building Deck")
    deck = create_from_csv('60_test1.csv')
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

def test_60_2():
    print("Building Deck")
    deck = create_from_csv('60_test2.csv')
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