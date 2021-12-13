class Card:
    """Magic the Gathering card
    cardname - title on card
    superytpe - the card's given type
    classification - Keyword representation
        threat
        resource
        cardadvantage
        removal
    cid - unique card identifier if multiple are in deck
    """
    __slots__ = ['cardname', 'supertype', 'classification', 'cid']

    def __init__(self, cardname, supertype, cid, classification):
        self.cardname = cardname
        self.supertype = supertype
        self.cid = cid
        self.classification = classification

    def __str__(self):
        return "{{{} | {} | {} | {}}}".format(self.cardname, self.supertype, self.classification, self.cid)

    def __repr__(self):
        return str(self)

    def type(self):
        """Returns the card's supertype"""
        return self.supertype

    def is_classified(self, c):
        """Returns true if the classification is valid"""
        return c == self.classification

