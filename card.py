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

