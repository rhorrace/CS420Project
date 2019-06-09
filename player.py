from calc import Calc
from deck import Deck

# Player class
class Player:
  # Initialize function
  def __init__(self):
    self._hand = []
    self._brain = Calc()

  # String function
  def __str__(self):
    player_hand = "Player:\t " + " ".join(str(c) for c in self._hand) + "\n"
    player_best = "\t " + str(self._brain)
    return player_hand + player_best

  # Receive cards function
  def receive(self, card):
    self._hand.extend(card)
    self._brain.add_cards(card)

  # Get hand function
  def get_hand(self):
    return self._hand

  # discard cards function
  def discard(self, to_discard):
    discarded_cards = [crd for crd in self._hand if str(crd) in to_discard]
    discarded = [str(crd) for crd in discarded_cards]
    self._hand = [crd for crd in self._hand if str(crd) not in discarded]
    self._brain.clear()
    self._brain.add_cards(self._hand)
    return discarded_cards

  # Give back hand function
  def put_back_hand(self):
    putback = self._hand.copy()
    self._hand = []
    self._brain.clear()
    return putback

  # Get cards from table function
  def look_at_table(self, cards):
    self._brain.add_cards(cards)

  # Get best hand function
  def best_hand(self):
    return self._brain.best_hand()

  # Get rank function
  def get_rank(self):
    return self._brain.get_rank()

  # Get rank as string function
  def get_rank_as_string(self):
    return str(self._brain)

# Dealer class, is also a player
class Dealer(Player):
  # Initialize function
  def __init__(self):
    super().__init__()
    self.__deck = Deck()
    self.__burned = []

  # String function
  def __str__(self):
    dealer_hand = "Dealer:\t " + " ".join(str(c) for c in self._hand) + "\n"
    dealer_best = "\t " + str(self._brain)
    return dealer_hand + dealer_best

  # Deal card(s) function
  def deal(self, n):
    return self.__deck.remove(n)

  # Burn card function
  def burn(self):
    self.__burned.extend(self.__deck.remove(1))

  # Retrieve card(s) function
  def retrieve_cards(self, cards):
    self.__deck.add(self.__burned)
    self.__burned = []
    self.__deck.add(cards)

