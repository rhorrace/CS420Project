# Card class
class Card:
  # Initialize function
  def __init__(self, name="Joker", suit="None", value=0):
    self.__name = name
    self.__suit = suit
    self.__value = value

  # Card is a specific name
  def is_a(self, name):
    return self.__name == name

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

  # Card as string, for print statements
  def __str__(self):
    return self.__name + ":" + self.__suit

  # Card as string, but works for lists too, for print statements
  def __repr__(self):
    return str(self)

  # Card hash for dictionaries
  def __hash__(self):
    return hash(self.__value)

  # == operator
  def __eq__(self, other):
    return self.__value == other.__value

  # != operator
  def __ne__(self, other):
    return self.__value != other.__value

  # < operator
  def __lt__(self, other):
    return self.__value < other.__value

  # <= operator
  def __le__(self, other):
    return self.__value <= other.__value

  # > operator
  def __gt__(self, other):
    return self.__value > other.__value

  # >= operator
  def __ge__(self, other):
    return self.__value >= other.__value

