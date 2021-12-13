class Card:
    """Magic the Gathering card
    cardname - title on card
    superytpe - the card's given type
    classification - list comprising of:
        ms - Manasource
        thr - Threat (default selection)
        ca - Card Advantage
        rm - Removal
    """
    __slots__ = ['cardname', 'supertype', 'classification']

    def __init__(self, cardname, supertype, classification = None):
        self.cardname = cardname
        self.supertype = supertype
        if not classification:
            self.classification = ['thr']
        else:
            self.classification = classification
    
    def type(self):
        """Returns the card's supertype"""
        return self.supertype

    def is_classified(self, c):
        """Returns true if the classification is valid"""
        return c in self.classification
    