# Card class
class Card:
  # Initialize function
  def __init__(self, name="Joker", suit="None", value=0):
    self.__name = name
    self.__suit = suit
    self.__value = value


  # Displays card
  def display(self):
    print(self.as_string())

  # Converts Card to string
  def as_string(self):
    return self.__name + ":" + self.__suit

  # Get Card name
  def get_name(self):
    return self.__name

  # Get Card suit
  def get_suit(self):
    return self.__suit

  # Get Card value
  def get_value(self):
    return self.__value

  # Get Card suit value
  def get_suit_val(self):
    return self.__suit_val

  def __eq__(self, other):
    return True if self.__value == other.__value else False

  def __ne__(self, other):
    return True if self.__value != other.__value else False

  def __lt__(self, other):
    return True if self.__value < other.__value else False

  def __le__(self, other):
    return True if self.__value <= other.__value else False

  def __gt__(self, other):
    return True if self.__value > other.__value else False

  def __ge__(self, other):
    return True if self.__value >= other.__value else False

c1 = Card("2", "H", 2)
c2 = Card("2", "D", 2)
print(c1 == c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)
print(c1 != c2)
