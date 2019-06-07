from table import Holdem, FiveDraw
import os

def play_holdem(game):
  os.system("clear")
  while True:
    game.play()
    choice = input("Continue) ENTER, Quit) Q: ")
    os.system("clear")
    if choice == "q" or choice == "Q": return

def play_five_card(game):
  os.system("clear")
  while True:
    game.play()
    phase = game.get_phase()
    choice = input("Continue) ENTER, Quit) Q: ").upper()
    if phase == 1 and choice != "Q":
      while True:
        choice = input("Would you like to replace cards (Y/N): ")
        choice = choice.upper()
        if choice == "Y" or choice == "N": break
      amount, cards = 0, []
      if choice == "Y":
        while True:
          amount = int(input("How many cards: "))
          if amount > 0 and amount <= 5: break
        while True:
          cards = input("Enter cards you want to replace (ex. 2:H 5:C etc.): ").upper().split()
          if len(cards) == amount: break
      game.draw(amount, cards)
    os.system("clear")
    if choice == "Q": return


if __name__ == "__main__":
  print("1) Texas Hold'em")
  print("2) 5-Card draw")
  print("Q) Quit")
  while True:
    choice = input("Enter Choice: ")
    if choice == "q" or choice == "Q":
      break
    elif choice.isdigit() and int(choice) > 0 and int(choice) < 3:
      break
  if choice == "1":
    play_holdem(Holdem())
  elif choice == "2":
    play_five_card(FiveDraw())
  print("Goodbye!")
