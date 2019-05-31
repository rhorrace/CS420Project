from calc import Calc
from deck import Deck

#Player States
playing = 0
allIn = 1
folded = 2

class Player:
  def __init__(self, start_money):
    self._hand = []       # list of cards
    self._brain = Calc()  # used to eval hand value
    self._money = start_money
    self.state = playing 

  def __str__(self):
    player_hand = "Player:\t " + " ".join(str(c) for c in self._hand) + "\n"
    player_best = "\t " + str(self._brain)
    return player_hand + player_best

  def receive(self, card):
    self._hand.extend(card)
    self._brain.add_cards(card)

  def discard(self, index):
    self._hand.remove(index)

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
    new_bet = int(input("Bet amount: "))
    if (new_bet == current_bet):
      print("\nCall!\n")
    if (new_bet >= self._money):
      print("\nAll-in!\n")
      current_bet = self._money
      self.state = allIn
    elif (new_bet <= 0):
      print("\nFold!\n")
      self.state = folded
      #folds should be handled by while loop check to see if the bet has changed
    return current_bet

  def send_bet(self, amount):
    if ((amount > self._money) or (self.state == folded)):
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

