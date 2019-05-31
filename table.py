from card import Card
from player import Player, Dealer

class Table:
  # initialize
  def __init__(self, max_hand=5):
    self._max_hand = max_hand
    self._phase = 0
    self._phases = 2
    self._pot = 0
    self._player = Player()
    self._dealer = Dealer()

  def play(self):
    if self._phase == 0: self.deal_phase()
    else:
      self.winner_phase()
      self.reset()
    self._phase = (self._phase + 1) % self._phases

  def deal_phase(self):
    self.deal_players()
    self.display_player()

  def winner_phase(self):
    self.display_player()
    self.display_dealer()
    self.winner()

  # Deal calds to each player
  def deal_players(self):
    for _ in range(self._max_hand):
       self._player.receive(self._dealer.deal(1))
       self._dealer.receive(self._dealer.deal(1))

  def reset(self):
    self._dealer.retrieve_cards(self._player.put_back_hand())
    self._dealer.retrieve_cards(self._dealer.put_back_hand())
    self._pot = 0

  # Displays player
  def display_player(self):
    print(self._player)
#    print("Player:\t", *self._player.get_hand(), sep=" ")
#    print("\t", self._player.get_rank_as_string(), ":\t", *self._player.best_hand(), sep=" ")

  # Displays dealer
  def display_dealer(self):
    print(self._dealer)
#    print("Dealer:\t", *self._dealer.get_hand(), sep=" ")
#    print("\t", self._dealer.get_rank_as_string(), ":\t", *self._dealer.best_hand(), sep=" ")

  # Determines who has the winning hand
  def winner(self):
    player_rank = self._player.get_rank()
    dealer_rank = self._dealer.get_rank()
    if player_rank > dealer_rank:
      print("Player wins")
      return self._player
    elif player_rank < dealer_rank:
      print("Dealer wins")
      return self._dealer
    else:
      return self.__tie_breaker()

  # Breaks the tie between player and dealer
  def __tie_breaker(self):
    player_hand = self._player.best_hand()
    dealer_hand = self._dealer.best_hand()
    player_hand = list(dict.fromkeys(player_hand))
    dealer_hand = list(dict.fromkeys(dealer_hand))
    for p,d in zip(player_hand, dealer_hand):
      if p > d:
        print("Player wins")
        return self._player
      elif p < d:
        print("Dealer wins")
        return self._dealer
    print("It's a Tie")

# 5draw, 5-card draw game, is a table.
class 5draw(Table):
  def __init__(self):
    super().__init__()
    self._player_discards = []
    self._dealer_discards = []
 
  def play(self):
    if self._phase == 0: self.deal_phase()
    elif self._phase == 1: self.discard_phase()
    else:
      self.winner_phase()
      self.reset()
    self._phase = self._phase+1

  def discard_phase(self):
    for i in self._player_discards:
      index_to_remove = self._player_discards[i]
      #I realize this will be wrong. Gotta go by card type/name, not index.
      self._player.discard(index_to_remove)
      self._player.receive(self._dealer.deal(1))
    for i in self._dealer_discards:
      index_to_remove = self._dealer_discards[i]
      self._dealer.discard(index_to_remove)
      self._dealer.receive(self._dealer.deal(1))

    # leaving ^^ for now, but I figure what I'll do is get the indexes from user,
    # get the cards names at those indexes from the hands
    # remove the cards with those names in the hands. 
    # that avoids removing the wrong cards    
  
# Holdem class, is a Table
class Holdem(Table):
  def __init__(self, max_hand=2):
    super().__init__(max_hand)
    self._phase = 0
    self._phases = 5
    self.__community = []

  # Reset function
  def reset(self):
    super().reset()
    self._dealer.retrieve_cards(self.__community)
    self.__community = []

  def play(self):
    if self._phase == 0: self.deal_phase()
    elif self._phase == 1: self.community_phase(3)
    elif self._phase == 2 or self._phase == 3: self.community_phase(1)
    else:
      self.winner_phase()
      self.reset()
    self._phase = (self._phase + 1) % self._phases

  def community_phase(self, n):
    self._dealer.burn()
    self.update_community(n)
    self.display_table()

  def winner_phase(self):
    self.display_table(show_dealer=True)
    winning_player = self.winner()
    if (winning_player == self._player):
      self._player._money += self._pot
    else:
      self._dealer._money += self._pot

  # Update community function
  def update_community(self,n):
    self.__community.extend(self._dealer.deal(n))
    self._player.look_at_table(self.__community[-n:])
    self._dealer.look_at_table(self.__community[-n:])

  # Displays the table (flop, turn, river)
  def display_table(self, show_dealer=False):
    self.display_community()
    self.display_player()
    if show_dealer:
      self.display_dealer()

  def display_community(self):
    num_cards = len(self.__community)
    if num_cards >= 3:
      print("Flop:\t", *self.__community[:3], sep=" ")
      if num_cards >= 4:
        print("Turn:\t", self.__community[3])
        if num_cards == 5:
          print("River:\t", self.__community[-1])

  def fill_pot(self, amount):
    self._pot += self._player.send_bet(amount)
    self._pot += self._dealer.send_bet(amount)

  def betting_phase(self):
    current_bet = 0
    final_bet = 0
    betting = 1
    while (betting == 1):
      current_bet = self._player.bet(current_bet)
      if (self._player.state == allIn):
        betting = 0
      else:
        current_bet = self._dealer.bet(current_bet)
      if ((current_bet <= final_bet) or (self._dealer.state == allIn)):
        betting = 0
      else:
        final_bet = current_bet 
    fill_pot(current_bet)

