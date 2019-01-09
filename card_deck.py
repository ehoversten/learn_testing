from random import shuffle

''' Implement Card Class ->
1) Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
2) Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
3) Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
'''
class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
        # return "{} of {}".format(self.value, self.suit)

''' Implement Deck Class ->
1) Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
2) Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
3) Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
4) Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
5) Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
6) Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
7) Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.
'''

class Deck:
    def __init__(self):
        suits  = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # CREATING NEW DECK USING LIST COMPREHENSION
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # print(self.cards)

        # CREATING NEW DECK USING NESTED FOR LOOPS 
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        #         print(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        # take the lowest value in [list]
        dealing = min([count, num])
        # for testing ...
        # print(f"dealing {dealing} cards")

        # No cards left in deck?
        if count == 0:
            raise ValueError("All cards have been dealt!")
        
        cards_in_deck = self.cards[-dealing:]
        self.cards = self.cards[:-dealing]
        return cards_in_deck

    def deal_card(self):
        # deal a single card (from the top of the deck) 
        return self._deal(1)[0]

    def deal_hand(self, size_hand):
        # Deal x number of cards 
        return self._deal(size_hand)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks may be shuffled")
        # use built-in shuffle function from random library
        shuffle(self.cards)
        # return instance if variable storage is needed
        return self

    def __repr__(self):
        return f"Deck of {self.count()} cards"
        # return "Deck of {} cards".format(self.cards)

new_deck = Deck()
# print(new_deck)
new_deck.shuffle()
card = new_deck.deal_card()
print(card)
hand = new_deck.deal_hand(5)
print(hand)
# new_deck._deal(52)
# print(new_deck.count())

num_cards_in_deck = new_deck.count()
print(num_cards_in_deck)