from card import Card
import numpy as np

class Deck:
  def __init__(self):
    self.__cards = []
    self.__build()

  def __build(self):
    names = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    suits = ["H","D","S","C"]
    for i in range(4):
      for j in range(13):
        card = Card(names[j],suits[i],values[j])
        self.__cards.append(card)
    np.random.shuffle(self.__cards)

  def get_cards(self):
    return self.__cards

  def display(self):
    for c in self.__cards:
      c.display()

  def add(self, cards):
    self.__cards.extend(cards)
    np.random.shuffle(self.__cards)

  def remove(self, n):
    cards = self.__cards[:n]
    self.__cards = self.__cards[n:]
    return cards
