from cards import *

from colorama import Fore,init

init(autoreset=True)

def consoleHello():
    print(Fore.MAGENTA + "Welcome to BlackJack!")
    print(Fore.CYAN + "\n----------------------------\n")
    print(Fore.LIGHTMAGENTA_EX + "Rules of the game: Your cards and the dealer's cards are dealt from decks.")
    print(Fore.LIGHTCYAN_EX + "You can request a card to improve your hand.")
    print(Fore.LIGHTCYAN_EX + "If the sum of the player's or dealer's cards exceeds 21, it's a bust!")
    print(Fore.LIGHTMAGENTA_EX + "The goal of the game is to score more points than the dealer, but not exceed 21.")
    print(Fore.CYAN + "\n----------------------------\n")

def run_game():
    global stPlN
    consoleHello()
    dialerCards()
    playerCards()
    giveCard()
    giveBotCard()
    giveCard()
    endGame()

if __name__ == "__main__":
    ask = 'y'
    while ask == 'y':
        run_game()
        ask = str(input(Fore.LIGHTCYAN_EX + 'New game? y/n (default y) ') or 'y')
