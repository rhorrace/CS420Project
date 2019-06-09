from card import Card

# Calculate hand class
class Calc:
  def __init__(self, cards=[]):
    self.__cards = []
    self.__suits = []
    self.__rank = 1
    self.__ranks = {1:"HighCard", 2:"OnePair", 3:"TwoPair", 4:"ThreeOfKind", 5:"Straight", 6:"Flush", 7:"FullHouse", 8:"FourOfKind", 9:"StraightFlush", 10:"RoyalFlush"}
    if cards: self.add_cards(cards)

  # String function
  def __str__(self):
    best = self.best_hand()
    hand_string = " ".join(str(c) for c in best)
    return self.__ranks[self.__rank] + ":\t" + hand_string

  # Clear function
  def clear(self):
    self.__cards = []
    self.__suits = []
    self.__rank = 1

  # Get rank function
  def get_rank(self):
    return self.__rank

  # Add cards to calc function
  def add_cards(self, cards):
    if not self.__cards:
      self.__cards = cards
    else:
      self.__cards.extend(cards)
    self.__cards = sorted(self.__cards, reverse=True)
    self.__calculate_rank()
    if not self.__rank in [5,9,10]:
      self.__cards = sorted(self.__cards, key=self.__cards.count, reverse=True)

  # Get best overall hand function
  def best_hand(self):
    if not self.__cards: return []
    hand = []
    if self.__rank == 10 or self.__rank == 9 or self.__rank == 6:
      filtered = list(filter(lambda c: c.get_suit() == self.__suits[0], self.__cards))
      hand = self.__get_straight(filtered) if self.__rank != 6 else filtered[:5]
    elif self.__rank == 5:
      hand = self.__get_straight(self.__cards)
    else: hand = self.__get_other()
    return hand

  # Get straight function
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

  # Get other best overall hand + kicker
  def __get_other(self):
    hand, kicker = [], []
    if self.__rank == 8 or self.__rank == 3:
      hand, kicker = self.__cards[:4], sorted(self.__cards[4:], reverse=True)[:1]
    elif self.__rank == 7:
      hand, kicker = self.__cards[:3], sorted(list(filter(lambda c: self.__cards[3:].count(c) >= 2, self.__cards[3:])), reverse=True)[:2]
    elif self.__rank == 4:
      hand, kicker = self.__cards[:3], sorted(self.__cards[3:],reverse=True)[:2]
    else:
      hand = self.__cards[:5]
    return hand + kicker

  # Calculate hand rank function
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

  # If flush function
  def __is_flush(self):
    self.__suits = [card.get_suit() for card in self.__cards]
    self.__mode_suit()
    suit_count = self.__suits.count(self.__suits[0])
    return suit_count >= 5

  # Most occuring suit function
  def __mode_suit(self):
    self.__suits = sorted(self.__suits)
    self.__suits = sorted(self.__suits, key=self.__suits.count, reverse=True)

  # Is straight function
  def __is_straight(self, cards):
    all_possible = list(dict.fromkeys(cards))
    if all_possible[0].is_a("A"):
      suit = all_possible[0].get_suit()
      all_possible.append(Card("A", suit, 1))
    prev = all_possible[0]
    count = 1
    for card in all_possible[1:]:
      count = count + 1 if card.get_value() == prev.get_value() - 1 else 1
      if count == 5:
        return True
      prev = card
    return False

  # Is other hand function
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

