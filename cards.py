from random import randint

from colorama import Fore,init

init(autoreset=True)

# Колода карт (включая масти)
allCards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', 'JH', 'QH', 'KH', 'AH',
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', 'JS', 'QS', 'KS', 'AS',
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', 'JD', 'QD', 'KD', 'AD',
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', 'JC', 'QC', 'KC', 'AC']

# Соответствующие значения карт
allCardsNum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10, 11,
               2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10, 11]

end = len(allCardsNum)

def dialerCards():
    end = len(allCardsNum)
    randNum = randint(0,end-1)

    rub = allCards.pop(randNum)
    rubN = allCardsNum.pop(randNum)
    if rub == 'AH':
        rubN = 1

    randNum2 = randint(0,end-1)

    rub2 = allCards.pop(randNum2)
    rubN2 = allCardsNum.pop(randNum2)
    if rub2 == 'AH':
        rubN2 = 1

    global stBotN
    stBotN = rubN+rubN2

    print(Fore.RED + 'Dealer cards:')
    global allBotCards
    allBotCards = rub + ' ' + rub2
    print(allBotCards)
    print(stBotN)

def playerCards():
    end = len(allCardsNum)
    randNum = randint(0, end - 1)

    rub = allCards.pop(randNum)
    rubN = allCardsNum.pop(randNum)
    if rub == 'AH':
        rubN = 1

    randNum2 = randint(0, end - 1)

    rub2 = allCards.pop(randNum2)
    rubN2 = allCardsNum.pop(randNum2)
    if rub2 == 'AH':
        rubN2 = 1

    global stPlN
    stPlN = rubN + rubN2

    print(Fore.LIGHTCYAN_EX + 'Player cards:')
    global allPlCards
    allPlCards = rub + ' ' + rub2
    print(allPlCards)
    print(stPlN)

def giveCard():
    global stPlN
    print(Fore.RED + 'Dealers cards:' + str(stBotN))
    print(Fore.RED + 'Player cards:' + str(stPlN))
    ask = str(input(Fore.LIGHTMAGENTA_EX + "Need a card? (default y): ") or "y")
    if ask == 'y':
        end = len(allCardsNum)
        randNum = randint(0, end - 1)

        rub = allCards.pop(randNum)
        rubN = allCardsNum.pop(randNum)
        stPlN += rubN

        global allPlCards
        allPlCards += ' ' + rub

        print('Player cards:')
        print(allPlCards)
        print(stPlN)

def giveBotCard():
    global stPlN
    global stBotN
    global allBotCards
    while stBotN < 17 :
        end = len(allCardsNum)
        randNum = randint(0, end - 1)

        rub = allCards.pop(randNum)
        rubN = allCardsNum.pop(randNum)
        stBotN += rubN

        allBotCards += ' ' + rub

    print('Dialer cards:')
    print(allBotCards)
    print(stBotN)


def endGame():
    if 21 >= stPlN > stBotN:
        print(Fore.GREEN + 'Player win' + ' ' + str(stPlN))
    elif stBotN == stPlN:
        print(Fore.YELLOW + 'pass')
    elif stPlN > 21:
        print(Fore.LIGHTRED_EX + 'Dealer win')
    elif stBotN > 21:
        print(Fore.GREEN + 'Player win')
    else:
        print(Fore.LIGHTRED_EX + 'Dealer win' + ' ' + str(stBotN))

