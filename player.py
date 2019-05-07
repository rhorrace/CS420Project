import calc as clc
import deck as dk

class Player:
  def __init__(self):
    self.__hand = []          #list of cards
    self._brain = clc.Calc() #used to eval hand value

  def recieve_card(self, new_card):
    self.__hand.append(new_card)

  def putback_hand(self):
    putback = self.__hand
    self.__hand = []
    return putback 

  def get_rank(self):
    self._brain.add_cards(self.__hand)
    return self._brain.get_rank()


class Dealer(Player):
  def __init__(self):
    super().__init__() #Simplified in Python3
    self.__deck = dk.deck() #For now has deck object, we can update it to work
                            #with however we end up having the dealer comm w/ deck
                            #(Likely w/ the table instead)
  def __deal_flop(self):
    deal = []
    for i in range(3):
      deal.append(self.__deck.deal_card())
    return deal
  
  def __deal_turn(self):
    return self.__deck.deal_card()

  def __deal_river(self): #for now keeping separate for nomenclature's sake
    return self.__deck.deal_card() #Not sure if it should be kept separate tho

  def deal(self):
    deal = []
	#deal cards to players here?
    deal.append(self.__deal_flop())
    #bets/folds/calls n' stuff here?
    deal.append(self.__deal_turn())
    #something here?
    deal.append(self.__deal_river())
    
'''
Note: 
This likely is not at all what the final version will be like.
I realize that the public "deal" method shouldn't even really be a thing.
Because, well, stuff has to happen in between dealing, say, the flop. So
the flop needs to be returned to the table before that. 
This was just a quick little implementation, and that's why I kept the
flop, turn and river separate (so they could be used properly when we have built
the table and what not)  
'''
