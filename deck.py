import card as crd
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
        c = crd.Card(names[j],suits[i],values[j])
        self.__cards.append(c)

  def display(self):
    for c in self.__cards:
      c.display()

  def deal_card(self):
    a_card = self.__cards.pop(0)
    #for testing purposes:
    print ("Popped: ")
    a_card.display()
    return a_card

  def shuffle(self):
    np.random.shuffle(self.__cards) 

d = Deck()
d.display()

d.shuffle()
d.deal_card()
