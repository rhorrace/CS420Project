import calc as calc

class Player:
  def __init__(self):
    self.__hand = []          #list of cards
    self._brain = calc.Calc() #used to eval hand value

  def recieve_card(self, new_card):
    self.__hand.append(new_card)

  def putback_hand(self):
    putback = self.__hand
    self.__hand = []
    return putback 

  def get_rank(self):
    self._brain.add_cards(self.__hand)
    return self._brain.get_rank()


