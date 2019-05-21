from table import Holdem
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

if __name__ == "__main__":
  play(Holdem())
  print("Goodbye!")
