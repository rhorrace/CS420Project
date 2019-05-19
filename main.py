import table as T
import os

def play(game):
  phases = 5
  phase = 0
  os.system("clear")
  while True:
    game.play()
    choice = input("Continue) ENTER, Quit) Q: ")
    os.system("clear")
    if choice == "q" or choice == "Q":
      return

game = T.Holdem()
play(game)
print("Goodbye!")
