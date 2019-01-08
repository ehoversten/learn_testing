''' Card Deck '''

class Card():

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __repr__(self):
        # return f"{val} of {suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck():

    pass
