from card import Card

class Calc:
  def __init__(self, cards=[]):
    self.__cards = []
    self.__suits = []
    self.__rank = 1
    self.__ranks = {1:"HighCard", 2:"OnePair", 3:"TwoPair", 4:"ThreeOfKind", 5:"Straight", 6:"Flush", 7:"FullHouse", 8:"FourOfKind", 9:"StraightFlush", 10:"RoyalFlush"}
    if cards: self.add_cards(cards)

  def __str__(self):
    return self.__ranks[self.__rank]

  def clear(self):
    self.__cards.clear()
    self.__suits.clear()
    self.__rank = 1

  def get_rank(self):
    return self.__rank

  def add_cards(self, cards):
    if not self.__cards:
      self.__cards = cards
    else:
      self.__cards.extend(cards)
    self.__cards = sorted(self.__cards, reverse=True)
    self.__calculate_rank()
    if not self.__rank in [5,9,10]:
      self.__cards = sorted(self.__cards, key=self.__cards.count, reverse=True)

  def best_hand(self):
    if not self.__cards:
      return []
    hand, kicker = [], []
    if self.__rank == 10 or self.__rank == 9:
      filtered = list(filter(lambda c: c.get_suit() == self.__suits[0], self.__cards))
      hand = self.__get_straight(filtered)
    elif self.__rank == 8 or self.__rank == 3:
      hand, kicker = self.__cards[:4], sorted(self.__cards[4:], reverse=True)[:1]
    elif self.__rank == 7:
      hand, kicker = self.__cards[:3], sorted(list(filter(lambda c: self.__cards[3:].count(c) >= 2, self.__cards[3:])), reverse=True)[:2]
    elif self.__rank == 6:
      hand = sorted([c for c in self.__cards if c.get_suit() == self.__suits[0]], reverse=True)[:5]
    elif self.__rank == 5:
      hand = self.__get_straight(self.__cards)
    elif self.__rank == 4:
      hand, kicker = self.__cards[:3], sorted(self.__cards[3:],reverse=True)[:2]
    else:
      hand = self.__cards[:min(len(self.__cards), 5)]
    return hand + kicker

  def __calculate_rank(self):
    num_cards = len(self.__cards)
    if not self.__cards:
      return
    if self.__is_flush():
      filtered = list(filter(lambda c: c.get_suit() == self.__suits[0], self.__cards))
      if self.__is_straight(filtered):
        self.__rank = 10 if (filtered[0].is_a("A") and filtered[4].is_a("10")) else 9
      else:
        self.__rank = 6
        if num_cards > 7:
          self.__is_other(num_cards)
    elif self.__is_straight(self.__cards):
        self.__rank = 5
        if num_cards > 7:
          self.__is_other(num_cards)
    else:
      self.__is_other(num_cards)

  def __is_flush(self):
    self.__suits = [card.get_suit() for card in self.__cards]
    self.__mode_suit()
    suit_count = self.__suits.count(self.__suits[0])
    return True if suit_count >= 5 else False

  def __mode_suit(self):
    self.__suits = sorted(self.__suits)
    self.__suits = sorted(self.__suits, key=self.__suits.count, reverse=True)

  def __is_straight(self, cards):
    all_possible = list(dict.fromkeys(cards))
    if all_possible[0].is_a("A"):
      suit = all_possible[0].get_suit()
      all_possible.append(Card("A", suit, 1))
    prev = all_possible[0]
    count = 1
    for card in all_possible[1:]:
      count = self.__count(card, prev, count)
      if count == 5:
        return True
      prev = card
    return False

  def __count(self, card1, card2, count):
    return count+1 if (card1.get_value() == card2.get_value()-1) else 1

  def __is_other(self, num_cards):
    cards = sorted(self.__cards, key=self.__cards.count, reverse=True)
    new_rank = 1
    if cards.count(cards[0]) == 4:
      new_rank = 8
    elif cards.count(cards[0]) == 3:
      if num_cards > 3:
        new_rank = 7 if (cards.count(cards[3]) >= 2) else 4
      else:
        new_rank = 4
    elif self.__cards.count(cards[0]) == 2:
      if num_cards <= 3:
        new_rank = 2
      else:
        new_rank = 3 if (cards.count(cards[2]) == 2) else 2
    self.__rank = max(self.__rank, new_rank)

  def __get_straight(self, cards):
    straight = []
    filtered = list(dict.fromkeys(cards))
    if filtered[0].is_a("A"):
      filtered.append(Card(filtered[0].get_name(), filtered[0].get_suit(), 1))
    straight.append(filtered[0])
    for card in filtered[1:]:
      if card.get_value() == straight[-1].get_value()-1:
        straight.append(card)
        if len(straight) == 5:
          return straight
      else:
        straight = [card]
    return []
