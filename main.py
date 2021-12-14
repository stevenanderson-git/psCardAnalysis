import random
from analysis import analyze_multihand
from card import Card
from deckbuilder import Deck
import csv
import collections
from plotstats import make_scatter


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


def create_generic_deck(resources, threats, removal, cardadvantage, deckname='Generic Deck'):
    """Creates a generic deck of resources, threats, removal, and cardadvantage
    Cards created have a generic supertype, names are their classification with the count they were created on
    and only taged based on classification.
    """
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


def generic_40():
    deckname = 'Generic 40'
    return create_generic_deck(16, 14, 5, 5, deckname=deckname)


def generic_60():
    deckname = 'Generic 60'
    return create_generic_deck(24, 20, 7, 9, deckname=deckname)


def generic_100():
    deckname = 'Generic 100'
    return create_generic_deck(40, 28, 16, 16, deckname=deckname)


def random_deck(totalcards):
    """Creates a randomized deck with the given total number of cards"""
    deckname = 'Randomized Deck'
    cardlist = []
    for i in range(totalcards):
        rng = random.randint(1, 4)
        if rng == 1:
            cardlist.append(Card('RESOURCE_' + str(i),
                            'generic', i, 'resource'))
        if rng == 2:
            cardlist.append(Card('THREAT_' + str(i), 'generic', i, 'threat'))
        if rng == 3:
            cardlist.append(Card('REMOVAL_' + str(i), 'generic', i, 'removal'))
        if rng == 4:
            cardlist.append(Card('CARDADVANTAGE_'+str(i),
                                 'generic', i, 'cardadvantage'))
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


def montehand_test_deck(deck, x, n):
    """Runs the provided deck through a Monty Carlo simulation x times drawing n cards as an opening hand."""
    mh = analyze_multihand(deck, x, n)
    counter = collections.Counter()
    for h in mh:
        counter.update(h)
    return dict(counter)


def random_deck_datagen():
    decks_to_create = 100
    deck_size = 100
    runs = 100
    starting_hand = 7
    # create a list of decks with a random distribution of deck_size cards
    dataset = [random_deck(deck_size) for i in range(decks_to_create)]
    results = [(d.type_distribution(), analyze_multihand(d,runs,starting_hand)) for d in dataset]
    xvals = []
    yvals = []
    for (dist, samp_hand) in results:
        for hand in samp_hand:
            xvals.append(dist['resource'])
            yvals.append(hand['resource'])
    
    make_scatter(xvals,yvals,'Deck Resources', 'Opening Hand Resources')




random_deck_datagen()

