import table as T
import os

def play_holdem(game):
  phases = 5
  phase = 0
  os.system("clear")
  while True:
    if phase == 0: game.deal_phase()
    elif phase == 1: game.community_phase(3)
    elif phase == 2 or phase == 3: game.community_phase(1)
    else:
      game.winner_phase()
      game.reset()
    choice = input("Continue) ENTER, Quit) Q: ")
    os.system("clear")
    if choice == "q" or choice == "Q":
      return
    phase = (phase + 1) % phases

game = T.Holdem()
play_holdem(game)
print("Goodbye!")
