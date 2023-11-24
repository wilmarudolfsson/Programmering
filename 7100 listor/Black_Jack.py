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

def print_cards(cards, hidden):
    
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


def blackjack_spel(deck):

    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    clear()

    while len(player_cards) < 2:

        player_card = random.choice(deck)
        player_cards.append()
        deck.remove(player_card)

        player_score += player_card.card_value

        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
        
        print("Spelarens kort: ")
        print_cards(player_cards, False)
        print("Spelare poäng = ", player_score)

        input()

        dealer_card = random.choise(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("Dealerns kort: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("Dealerns poäng = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("Dealerns poäng = ", dealer_score - dealer_cards[-1].card_value)

        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
            
        input()

    if player_score == 21:
        print("SPELAREN HAR BLACKJACK!!!")
        print("SPELAREN VINNER!!")
        quit()
    
    clear()

    print("Dealerns kort: ")
    print_cards(dealer_cards[:-1], True)
    print("Dealerns poäng = ", dealer_score-dealer_cards[-1].card_value)

    print()

    print("Spelarens kort: ")
    print_cards(player_cards, False)
    print("Spelarens poäng = ",player_score)
    

    while player_score < 21:
        choice = input("Skriv in H för Hit eller S för Stand: ")

        if len(choice) !=1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Fel svar!!! Försök igen")

        if choice.upper() == 'H':

            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            player_score += player_card.card_value

            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card.value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1
            
            clear()

            print("Dealerns kort: ")
            print_cards(dealer_cards[:-1], True)
            print("Dealerns poäng = ", dealer_score - dealer_cards[-1].card.value)

            print()

            print("Spelarens kort: ")
            print_cards(player_cards, False)
            print("Spelarens poäng = ", player_score)

        if choice.upper() == 'S':
            break


        clear()

        print("Spelarens kort: ")
        print_cards(player_cards, False)
        print("Spelarens poäng = ", player_score)

        print()
        print("Dealern avslöjar korten...")

        print("Dealerns kort: ")
        print_cards(dealer_cards, False)
        print("Dealerns poäng = ", dealer_score)

        if player_score == 21:
            print("Spelaren har BlackJack")
            quit()

        if player_score > 21:
            print("Spelaren har blivit tjock!! Spelet är slut")
            quit()

        input()

        while dealer_score < 17:
            clear()

            print("Dealern har bestämt sig för Hit....")

            dealer_card = random.choice(deck)
            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            dealer_score += dealer_card.card_value

            while dealer_score > 21 and c < len(dealer_cards):
                if dealer_cards[c].card_value == 11:
                    dealer_cards[c].card.value = 1
                    dealer_score -= 10
                    c += 1
                else:
                    c += 1
            

            print("Spelarens poäng: ")
            print_cards(player_cards, False)
            print("Spelarens poäng = ", player_score)

            print()

            print("Dealerns kort: ")
            print_cards(dealer_cards, False)
            print("Dealerns poäng = ", dealer_score)

            input()

        #dealern bust
        



