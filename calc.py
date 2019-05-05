import card as crd
import numpy as np
from scipy import stats

def partition(cards, l, h):
  i = l - 1
  pivot = card[h]
  for j in range(l, h):
    if(cards[i] <= pivot):
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i + 1

def sort(card, l, h):
  if(l < h):
    p = partition(cards, l ,h)
    quicksort(cards,l,p-1)
    quicksort(cards, p+1, h)



class Calc:
  def __init__(self):
    self.__cards = []

  def add_hand(self,cards):
    self.__cards = cards

  def add_cards(self, cards):
    self.__cards = np.append(self.__cards, cards)
    sort(self.__cards, 0, self.__cards.size-1)

  def calculate(self):
    self.__is_straight(self.__cards)
    return 0

  def __is_flush(self):
    suits = [card.get_suit() for ard in cards]
    suit = self.__max_suit(suits)
    suit_count = np.size(suits == suit)
    return True, suit if suit_count >= 5 else False, None

  def __max_suit(self, suits):
    return stats.mode(suit)

  def __is_straight(self, cards):
    all_possible = np.flip(np.unique(cards))
    if(all_possible[0].is_a("A")):
      suit = all_possible[0].get_suit()
      all_possible = np.append(all_possible, c.Card("A", suit, 1)).tolist()
    prev = all_possible[0]
    count = 1
    for card in all_possible[1:]:
      if(count == 5):
        return True
      count = self.__count(card, prev, count)
      prev = card
    return False

  def __count(self, card1, card2, count):
    return count+1 if (card.get_value() == prev.get_value()-1) else 1

  def __get_flush(self, cards, suit):
    return list(filter(lambda c: c.get_suit() == suit, cards)).reverse()

  def __get_straight(self, cards):
    straight = []
    all_possible = np.flip(np.unique(cards))
    if(all_possible[0].is_a("A")):
      suit = all_possible[0].get_suit()
      all_possible = np.append(all_possible, c.Card("A", suit, 1)).tolist()
    for card in all_possible:
      if(not straight):
        straight.append(card)
      elif(len(striaght) == 5):
        break
      else:
        if(card == straight[-1].get_value()-1):
          straight.append(card)
        else:
          straight = [card]
    return straight

  def __get_four_of_kind(self, cards):
    groups = self.__group_sorted(cards)
    fours = groups[0:4]
    kicker = sorted(groups[4:]).reverse()[0]
    fours.append(kicker)
    return fours

  def __get_full_house(self, cards):
    groups = self.__group_sorted(cards)
    threes = groups[0:3]
    pairs = sorted([c for c in groups[3:] if groups.count(c) >= 2]).reverse()[0:2]
    return threes + pairs

  def __get_three_of_kind(self, cards)
    groups = self.__group_sorted(cards)
    threes = groups[0:3]
    pairs = sorted(groups[3:]).reverse()[0:2]
    return threes + pairs

  def __get_two_pairs(self, cards):
    groups = self.__group_sorted(cards)
    pairs = group[0:4]
    kicker = sorted(groups[4:]).reverse()[0]
    return pairs + kicker

  def __get_one_pair(self, cards):
    groups = self.__group_sorted(cards)
    pairs = group[0:4]
    kicker = sorted(groups[4:]).reverse()[0]
    return pairs + kicker

  def __get_high_card(self, cards):
    return sorted(cards).reverse()[0:5]

  def __group_sorted(self, cards):
    return sorted(new_cards, key=new_cards.count).reverse()



