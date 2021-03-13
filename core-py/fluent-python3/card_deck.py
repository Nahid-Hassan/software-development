import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # return: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    # return: ['spades', 'diamonds', 'clubs', 'hearts']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    # return the len of the _cards
    def __len__(self):
        return len(self._cards)

    # now we can perform indexing, slicing, iteration operation
    # easily.
    # to understand the effect just comment out this function
    # and try to perform above "slicing, indexing or iteration"
    # operation
    def __getitem__(self, position):
        return self._cards[position]


# create a deck FrenchDeck object with 52 Card item.
deck = FrenchDeck()

# print total len of deck object
print(len(deck))

# randomly chose single card from the deck
print("Random: ", choice(deck))

# Indexing Operation
print(deck[0])  # access first items
print(deck[-1])  # access last items

# Slicing operation
print(deck[:3])  # first 3 columns
print(deck[12::13])

# Iterable
i = 0
for card in deck:
    print(card)
    i = i + 1
    # show only first 5 results
    if (i == 5):
        i = 0
        break

# Iterable in reverse
for card in reversed(deck):
    print(card)
    i = i + 1
    # show only first 5 results
    if (i == 5):
        i = 0
        break

# Iteration is often implicit. If a collection has no __contains__ method, the in operator
# does a sequential scan.
print(dir(deck))
if '__contains__' in dir(deck):
    print('Okay')
else:
    print('Not found')

# result is not found
# so now we confidently say here in does a sequential scan. hence deck is an iterator

print(Card('Q', 'hearts') in deck)  # True
print(Card('M', 'hearts') in deck)  # False

# sorting deck
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    print(card)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
