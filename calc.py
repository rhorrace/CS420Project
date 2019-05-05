import card as crd
import numpy as np
from scipy import stats

def partition(cards, l, h):
  i = l - 1
  pivot = cards[h]
  for j in range(l, h):
    if(cards[j] <= pivot):
      i += 1
      cards[i], cards[j] = cards[j], cards[i]
  cards[i+1], cards[h] = cards[h], cards[i+1]
  return i + 1

def sort(cards, l, h):
  if(l < h):
    p = partition(cards, l ,h)
    sort(cards,l,p-1)
    sort(cards, p+1, h)


class Calc:
  def __init__(self):
    self.__cards = []
    self.__suits = []
    self.__rank = 1
    self.__ranks = {1:"HighCard", 2:"OnePair", 3:"TwoPair", 4:"ThreeOfKind", 5:"Straight", 6:"Flush", 7:"FullHouse", 8:"FourOfKind", 9:"StraightFlush", 10:"RoyalFlush"}

  def __str__(self):
    return self.__ranks.get(self.__rank)

  def add_cards(self, cards):
    self.__cards = np.append(self.__cards, cards)
    sort(self.__cards, 0, self.__cards.size-1)
    self.__cards = self.__cards.tolist()
    self.calculate_rank()

  def calculate_rank(self):
    if(self.__is_flush()):
      filtered = list(filter(lambda c: c.get_suit() == self.__suits[-1], self.__cards))
      if(self.__is_straight(filtered)):
        self.__rank = 10 if (filtered[-1].is_a("A") and filtered[-5].is_a("10")) else 9
      else:
        self.__rank = 6
        self.__is_other()
    elif(self.__is_straight(self.__cards)):
        self.__rank = 5
    else:
      self.__is_other()

  def __is_flush(self):
    self.__suits = [card.get_suit() for card in self.__cards]
    self.__mode_suit()
    suit_count = self.__suits.count(self.__suits[-1])
    return True if suit_count >= 5 else False

  def __mode_suit(self):
    self.__suits = sorted(self.__suits)
    self.__suits = sorted(self.__suits, key=self.__suits.count)

  def __is_straight(self, cards):
    all_possible = np.flip(np.unique(cards))
    if(all_possible[0].is_a("A")):
      suit = all_possible[0].get_suit()
      all_possible = np.append(all_possible, crd.Card("A", suit, 1)).tolist()
    prev = all_possible[0]
    count = 1
    for card in all_possible[1:]:
      count = self.__count(card, prev, count)
      if(count == 5):
        return True
      prev = card
    return False

  def __count(self, card1, card2, count):
    return count+1 if (card1.get_value() == card2.get_value()-1) else 1

  def __is_other(self):
    grouped = sorted(self.__cards, key=self.__cards.count)
    new_rank = 1
    if(grouped.count(grouped[-1]) == 4):
      new_rank = 8
    elif(grouped.count(grouped[-1]) == 3):
      new_rank = 7 if (grouped.count(grouped[-4]) >= 2) else 4
    elif(grouped.count(grouped[-1]) == 2):
      if(len(grouped) == 2):
        new_rank = 2
      else:
        new_rank = 3 if (grouped.count(grouped[-3]) == 2) else 2
    self.__rank = max(self.__rank, new_rank)
