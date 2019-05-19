import card as crd
import player as p

class Table:
  # initialize
  def __init__(self):
    self._player = p.Player()
    self._dealer = p.Dealer()

  # Deal calds to each player
  def deal_players(self, n):
    for _ in range(n):
       self._player.receive(self._dealer.deal(1))
       self._dealer.receive(self._dealer.deal(1))


  # Displays players and dealer
  def display_players(self):
    print("Player:\t", self._player.get_hand())
    print("\t", self._player.get_rank_as_string(), ":\t", self._player.best_hand())
    print("Dealer:\t", self._dealer.get_hand())
    print("\t", self._dealer.get_rank_as_string(), ":\t", self._dealer.best_hand())


  # Detemrines who has the winning hand
  def winner(self):
    player_rank = self._player.get_rank()
    dealer_rank = self._dealer.get_rank()
    if player_rank > dealer_rank:
      print("Player wins")
    elif player_rank < dealer_rank:
      print("Dealer wins")
    else:
      self.__tie_breaker()

  # Breaks the tie between player and dealer
  def __tie_breaker(self):
    player_hand = self._player.best_hand()
    dealer_hand = self._dealer.best_hand()
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

class Holdem(Table):
  def __init__(self):
    super().__init__()
    self.__community = []

  # Flop function
  def update_community(self,n):
    self.__community.extend(self._dealer.deal(n))
    self._player.look_at_table(self.__community[-n:])
    self._dealer.look_at_table(self.__community[-n:])

  # Displays the table (flop, turn, river)
  def display_table(self):
    num_cards = len(self.__community)
    if num_cards >= 3:
      print("Flop:\t", self.__community[:3])
      if num_cards >= 4:
        print("Turn:\t", self.__community[3:4])
        if num_cards == 5:
          print("River:\t", self.__community[-1:])

  #Runs through a complete game
  def play_game(self, n):
    t.deal_players(n)
    t.display_players()
    t.display_table()
    print("---------------------")
    t.update_community(3)
    t.display_table()
    t.display_players()
    print("---------------------")
    t.update_community(1)
    t.display_table()
    t.display_players()
    print("---------------------")
    t.update_community(1)
    t.display_table()
    t.display_players()
    print("---------------------")
    t.winner()


t = Holdem()
max_hand = 2
t.play_game(2)
