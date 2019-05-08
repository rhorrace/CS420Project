import calc as clc
import deck as dk

class Player:
  def __init__(self):
    self.__hand = []          #list of cards
    self._brain = clc.Calc() #used to eval hand value

  def receive_card(self, new_card):
    self.__hand.append(new_card)

  def putback_hand(self):
    putback = self.__hand
    self.__hand = []
    return putback

  def get_rank(self):
    self._brain.add_cards(self.__hand)
    return self._brain.get_rank()


class Dealer(Player):
  def __init__(self):
    super().__init__() #Simplified in Python3
    self.__deck = dk.deck() #For now has deck object, we can update it to work
                            #with however we end up having the dealer comm w/ deck
                            #(Likely w/ the table instead)
  def deal(self, n):
    return self.__deck.remove(n)

  def retrieve(self, cards):
    self.__deck.add(cards)
