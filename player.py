from calc import Calc
from deck import Deck

class Player:
  def __init__(self, start_money):
    self._hand = []          # list of cards
    self._brain = Calc()  # used to eval hand value
    self._money = start_money

  def __str__(self):
    player_hand = "Player:\t " + " ".join(str(c) for c in self._hand) + "\n"
    player_best = "\t " + str(self._brain)
    return player_hand + player_best

  def receive(self, card):
    self._hand.extend(card)
    self._brain.add_cards(card)

  def get_hand(self):
    return self._hand

  def put_back_hand(self):
    putback = self._hand.copy()
    self._hand = []
    self._brain.clear()
    return putback

  def look_at_table(self, cards):
    self._brain.add_cards(cards)

  def best_hand(self):
    return self._brain.best_hand()

  def get_rank(self):
    return self._brain.get_rank()

  def get_rank_as_string(self):
    return str(self._brain)

  def bet(self, current_bet):
    if ((2*current_bet) > self._money):
      return current_bet
    return (2*current_bet)
    #I don't actually know how to get user input in py
    #The wiki says raises usually are 2x so for now, if
    #they can't raise 2x, they fold (ret current_bet)

  def send_bet(self, amount):
    if (amount > self._money):
      return 0
    self._money -= amount
    return amount


# Dealer class, is also a player
class Dealer(Player):
  # Initialize
  def __init__(self, start_money):
    super().__init__(start_money)
    self.__deck = Deck()
    self.__burned = []

  def __str__(self):
    dealer_hand = "Dealer:\t " + " ".join(str(c) for c in self._hand) + "\n"
    dealer_best = "\t " + str(self._brain)
    return dealer_hand + dealer_best

  def deal(self, n):
    return self.__deck.remove(n)

  def burn(self):
    self.__burned.extend(self.__deck.remove(1))

  def retrieve_cards(self, cards):
    self.__deck.add(self.__burned)
    self.__burned = []
    self.__deck.add(cards)

