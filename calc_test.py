import unittest
from calc import Calc
from card import Card

# Unit tests for Calc class
class CalcTest(unittest.TestCase):
  def test_str(self):
    test_calc = Calc()
    self.assertEqual(str(test_calc), "HighCard")

  def test_get_rank(self):
    test_calc = Calc()
    self.assertEqual(test_calc.get_rank(), 1)

  def test_high_card(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","S",6), Card("7", "D",7), Card("8","S",8), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 1)
    self.assertEqual(str(test_calc), "HighCard")
    self.assertEqual(test_calc.best_hand(), result)

  def test_one_pair(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","S",6), Card("6", "D",6), Card("8","S",8), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)
    result = sorted(result, key=result.count, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 2)
    self.assertEqual(str(test_calc), "OnePair")
    self.assertEqual(test_calc.best_hand(), result)

  def test_two_pair(self):
    hand = [Card("2", "H", 2), Card("4","D",4), Card("4","H",4), Card("6","S",6), Card("6", "D",6), Card("8","S",8), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)
    result = sorted(result, key=result.count, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 3)
    self.assertEqual(str(test_calc), "TwoPair")
    self.assertEqual(test_calc.best_hand(), result)

  def test_three_of_kind(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","C",6), Card("6", "D",6), Card("6","S",6), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)
    result = sorted(result, key=result.count, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 4)
    self.assertEqual(str(test_calc), "ThreeOfKind")
    self.assertEqual(test_calc.best_hand(), result)

  def test_straight(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","S",6), Card("5", "D",5), Card("8","S",8), Card("A", "D", 14)]
    result = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","S",6), Card("5", "D",5)]
    result = sorted(result, reverse=True)
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 5)
    self.assertEqual(str(test_calc), "Straight")
    self.assertEqual(test_calc.best_hand(), result)

  def test_flush(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","H",6), Card("7", "H",7), Card("8","S",8), Card("A", "H", 14)]
    result = [c for c in hand if c.get_suit() == "H"]
    result = sorted(result, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 6)
    self.assertEqual(str(test_calc), "Flush")
    self.assertEqual(test_calc.best_hand(), result)

  def test_full_house(self):
    hand = [Card("A", "H", 14), Card("A","H",14), Card("4","H",4), Card("6","C",6), Card("6", "D",6), Card("6","S",6), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)
    result = sorted(result, key=result.count, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 7)
    self.assertEqual(str(test_calc), "FullHouse")
    self.assertEqual(test_calc.best_hand(), result)

  def test_four_of_kind(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("6","H",6), Card("6","C",6), Card("6", "D",6), Card("6","S",6), Card("A", "D", 14)]
    result = sorted(hand, reverse=True)
    result = sorted(result, key=result.count, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 8)
    self.assertEqual(str(test_calc), "FourOfKind")
    self.assertEqual(test_calc.best_hand(), result)

  def test_straight_flush(self):
    hand = [Card("2", "H", 2), Card("3","H",3), Card("4","H",4), Card("6","H",6), Card("5", "H",5), Card("6","S",6), Card("A", "D", 14)]
    result = [c for c in hand if c.get_suit() == "H"][:5]
    result = sorted(result, reverse=True)
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 9)
    self.assertEqual(str(test_calc), "StraightFlush")
    self.assertEqual(test_calc.best_hand(), result)

  def test_royal_flush(self):
    hand = [Card("10", "H", 10), Card("Q","H",12), Card("9","H",9), Card("J","H",11), Card("K", "H",13), Card("6","S",6), Card("A", "H", 14)]
    result = [c for c in hand if c.get_suit() == "H"]
    result = sorted(result, reverse=True)[:5]
    test_calc = Calc(hand)
    self.assertEqual(test_calc.get_rank(), 10)
    self.assertEqual(str(test_calc), "RoyalFlush")
    self.assertEqual(test_calc.best_hand(), result)


if __name__ == "__main__":
  unittest.main()
