import random
import os
import time


class Card:
    def __init__(self, suit, value, card_value):


        self.suit = suit

        self.value = value

        self.card_value = card_value

def clear():
    os.system("clear")

def print_cards(cards, hidden)
    
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)


    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}            |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s) 

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)   

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()


def blackjack_spel(kortlek):

    spelare_korten = []
    dealern_korten = []

    spelare_poäng = 0
    dealern_poäng = 0

    clear()

    while len(spelare_korten) < 2:

        spelare_kort = random.choice(kortlek)
        spelare_korten.append(spelare_kort)
        kortlek.remove(spelare_kort)

        spelare_poäng += spelare_kort.card_value

        if len(spelare_korten) == 2:
            if spelare_korten[0].card_value == 11 and spelare_korten[1].card_value == 11:
                spelare_korten[0].card_value = 1
                spelare_poäng -= 10
        
        print("Spelarens kort: ")
        print_cards(spelare_korten, False)
        print("Spelare poäng = ", spelare_poäng)

        input()

        dealern_kort = random.choise(kortlek)
        dealern_korten.append(dealern_kort)
        kortlek.remove(dealern_kort)

        dealern_poäng += dealern_kort.card_value

        print("Dealerns kort: ")
        if len(dealern_korten) == 1:
            print_cards(dealern_korten, False)
            print("Dealerns poäng = ", dealern_poäng)
        else:
            print_cards(dealern_korten[:-1], True)
            print("Dealerns poäng = ", dealern_poäng - dealern_korten[-1].card_value)

        if len(dealern_korten) == 2:
            if dealern_korten[0].card_value == 11 and dealern_korten[1].card_value == 11:
                dealern_korten[1].card_value = 1
                dealern_poäng -= 10
            
        input()

    if spelare_poäng == 21:
        print("SPELAREN HAR BLACKJACK!!!")
        print("SPELAREN VINNER!!")
        quit()
    
    clear()

    print("Dealerns kort: ")
    print_cards(spelare_korten,[:-1], True)
    print("Dealerns poäng = ", dealern_poäng-dealern_korten[-1].card_value)

    print()
    
