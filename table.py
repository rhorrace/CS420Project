import card as crd
import player as p

class Table:
  # initialize
  def __init__(self):
    self.__player = p.Player()
    self.__dealer = p.Dealer()
    self.__cards = []

  # Deal calds to each player
  def deal_players(self):
    for _ in range(2):
       self.__player.receive(self.__dealer.deal(1))
       self.__dealer.receive(self.__dealer.deal(1))

  # Flop function
  def flop(self):
    self.__cards.extend(self.__dealer.deal(3))
    self.__player.look_at_table(self.__cards)
    self.__dealer.look_at_table(self.__cards)

  # Turn function
  def turn(self):
    self.__cards.extend(self.__dealer.deal(1))
    self.__player.look_at_table(self.__cards[-1:])
    self.__dealer.look_at_table(self.__cards[-1:])

  # River fucntion
  def river(self):
    self.__cards.extend(self.__dealer.deal(1))
    self.__player.look_at_table(self.__cards[-1:])
    self.__dealer.look_at_table(self.__cards[-1:])

  # Displays players and dealer
  def display_players(self):
    print("Player\n\t", self.__player.get_rank_as_string(), " ", self.__player.best_hand())
    print("Dealer\n\t", self.__dealer.get_rank_as_string(), " ", self.__dealer.best_hand())

  # Displays the table (flop, turn, river)
  def display_table(self):
    num_cards = len(self.__cards)
    if num_cards >= 3:
      print("Flop:\t", self.__cards[:3])
      if num_cards >= 4:
        print("Turn:\t", self.__cards[3:4])
        if num_cards == 5:
          print("River:\t", self.__cards[-1:])

  # Detemrines who has the winning hand
  def winner(self):
    player_rank = self.__player.get_rank()
    dealer_rank = self.__dealer.get_rank()
    if player_rank > dealer_rank:
      print("Player wins")
    elif player_rank < dealer_rank:
      print("Dealer wins")
    else:
      self.__tie_breaker()

  # Breaks the tie between player and dealer
  def __tie_breaker(self):
    player_hand = self.__player.best_hand()
    dealer_hand = self.__dealer.best_hand()
    player_hand = list(dict.fromkeys(player_hand))
    dealer_hand = list(dict.fromkeys(dealer_hand))
    for p,d in zip(player_hand,dealer_hand):
      if p > d:
        print("Player wins")
        return
      elif p < d:
        print("Dealer wins")
        return
    print("It's a Tie")

t = Table()
t.deal_players()
t.display_players()
t.display_table()
print("\n")
t.flop()
t.display_table()
t.display_players()
print("\n")
t.turn()
t.display_table()
t.display_players()
print("\n")
t.river()
t.display_table()
t.display_players()
print("\n")
t.winner()
