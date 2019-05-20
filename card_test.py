import unittest
from card import Card

class CardTest(unittest.TestCase):
  def test_is_a(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(test_card.is_a("A"), True)
    self.assertEqual(test_card.is_a("10"), False)

  def test_as_string(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(test_card.as_string(), "A:H")

  def test_str(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(str(test_card), "A:H")

  def test_get_name(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(test_card.get_name(), "A")

  def test_get_suit(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(test_card.get_suit(), "H")

  def test_get_value(self):
    test_card = Card("A", "H", 14)
    self.assertEqual(test_card.get_value(), 14)

  def test_eq(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 == card2, True)
    self.assertEqual(card1 == card3, False)

  def test_ne(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 != card2, False)
    self.assertEqual(card1 != card3, True)

  def test_lt(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 < card2, False)
    self.assertEqual(card1 < card3, False)
    self.assertEqual(card3 < card1, True)

  def test_le(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 <= card2, True)
    self.assertEqual(card1 <= card3, False)
    self.assertEqual(card3 <= card1, True)

  def test_gt(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 > card2, False)
    self.assertEqual(card1 > card3, True)
    self.assertEqual(card3 > card1, False)

  def test_ge(self):
    card1 = Card("A", "H", 14)
    card2 = Card("A", "H", 14)
    card3 = Card("K", "H", 13)
    self.assertEqual(card1 >= card2, True)
    self.assertEqual(card1 >= card3, True)
    self.assertEqual(card3 >= card1, False)

if __name__ == "__main__":
  unittest.main()
