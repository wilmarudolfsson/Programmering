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
            s = s + "\t|  {}             |".format(card.value)
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


def blackjack_game(deck):

    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    clear()

    while len(player_cards) < 2:

        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        player_score += player_card.card_value

        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
        
        print("DINA KORT: ")
        print_cards(player_cards, False)
        print("DINA POÄNG = ", player_score)

        input()

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("DEALERNS KORT: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALERNS POÄNG = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("DEALERNS POÄNG = ", dealer_score - dealer_cards[-1].card_value)

        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
            
        input()

    if player_score == 21:
        print("DU HAR HAR BLACKJACK!!!")
        print("DU VINNER!!!")
        quit()
    
    clear()

    print("DEALERNS KORT: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALERNS POÄNG = ", dealer_score-dealer_cards[-1].card_value)

    print()

    print("DINA KORT: ")
    print_cards(player_cards, False)
    print("DINA POÄNG = ",player_score)
    

    while player_score < 21:
        choice = input("Skriv in H för Hit eller S för Stand: ")

        if len(choice) !=1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("FEL SVAR!!! FÖRSÖK IGEN!!")

        if choice.upper() == 'H':

            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            player_score += player_card.card_value

            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1
            
            clear()

            print("DEALERNS KORT: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALERNS POÄNG = ", dealer_score - dealer_cards[-1].card_value)

            print()

            print("DINA KORT: ")
            print_cards(player_cards, False)
            print("DINA POÄNG = ", player_score)

        if choice.upper() == 'S':
            break

        clear()

        print("DINA KORT: ")
        print_cards(player_cards, False)
        print("DINA POÄNG = ", player_score)

        print()
        print("DEALERN AVSLÖJAR KORTEN......")

        print("DEALERNS KORT: ")
        print_cards(dealer_cards, False)
        print("DEALERNS POÄNG = ", dealer_score)

        if player_score == 21:
            print("DU HAR BLACKJACK")
            quit()

        if player_score > 21:
            print("DU HAR BLIVIT TJOCK!!!SPELET ÄR SLUT")
            quit()

        input()

        while dealer_score < 17:
            clear()

            print("DEALERN HAR BESTÄMT SIG FÖR HIT....")

            dealer_card = random.choice(deck)
            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            dealer_score += dealer_card.card_value

            c = 0
            while dealer_score > 21 and c < len(dealer_cards):
                if dealer_cards[c].card_value == 11:
                    dealer_cards[c].card.value = 1
                    dealer_score -= 10
                    c += 1
                else:
                    c += 1
            

            print("DINA KORT: ")
            print_cards(player_cards, False)
            print("DINA POÄNG = ", player_score)

            print()

            print("DEALERNS KORT: ")
            print_cards(dealer_cards, False)
            print("DEALERNS POÄNG = ", dealer_score)

            input()

        #dealern bust
        if dealer_score > 21:
            print("DEALERN HAR BLIVIT TJOCK!!! DU VINNER!!!")
            quit()

        if dealer_score == 21:
            print("DEALERN HAR FÅTT BLACKJACK!! DU FÖRLORADE!!")
            quit()

        if dealer_score == player_score:
            print("DET BLEV OAVGJORT!!!")

        elif player_score > dealer_score:
            print("DU VANN!!!")

        else:
            print("DEALERN VANN!!!")

if __name__ == '__main__':

    suits = ["Spades", "Hearts", "Clubs", "Dimonds"]

    suits_values = {"Spades":"\u2664", "Hearts":"\u2661","Clubs":"\u2667", "Dimonds":"\u2662"}

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    cards_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10 }

    deck =[]

    for suit in suits:

        for card in cards:
            
            deck.append (Card(suits_values[suit], card, cards_values[card])) 

    blackjack_game(deck)   



