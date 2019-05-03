class Card:
  def __init__(self, name="Joker", suit="None", value=0):
    self.name = name
    self.suit = suit
    self.value = value

  def display(self):
    print(self.as_string())

  def as_string(self):
    return self.name + ":" + self.suit

  def get_name(self):
    return self.name

  def get_suit(self):
    return self.suit

  def get_value(self):
    return self.value

c = Card("2","H",2)
c.display()
c = Card("3","H",2)
c.display()
c = Card("4","H",2)
c.display()
