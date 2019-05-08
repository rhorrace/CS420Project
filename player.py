import calc as clc
import deck as dk

class Player:
  def __init__(self):
    self.__hand = []          # list of cards
    self._brain = clc.Calc()  # used to eval hand value

  def receive_card(self, card):
    self.__hand.append(card)
    self._brain.add_cards(card)

  def putback_hand(self):
    return self.__hand.pop(2)

  def look_at_table(self, cards):
    self._brain.add_cards(card)

  def get_rank(self):
    return self._brain.get_rank()

  def get_rank_as_string(self):
    return self._brain.as_string()

# Dealer class, is also a player
class Dealer(Player):
  # Initialize
  def __init__(self):
    super().__init__()
    self.__deck = dk.Deck()

  def deal(self, n):
    return self.__deck.remove(n)

  def retrieve_cards(self, cards):
    self.__deck.add(cards)

