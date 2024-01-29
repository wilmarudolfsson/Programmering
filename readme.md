Loggbok
===========
24 01 29
-------------
### Tkinter

Idag har jag kollat igenom kod för att se vad jag ska göra för mitt yatzy spel. Jag har också gjort en lista i nummer ordning om vad jag ska göra först.

### Vad jag vill att mitt Yatzy spel ska göra:

1. Slå tärningar
2. Välja vilka tärningar man vill behålla
3. Slå om tärningarna
4. Välj vilka tärningar man vill behålla
5. Slå om tärningarna



24 01 26
-------------
### Tkinter

Fick löst så att tre i rad spelet fungerar och ska nu läsa och lära mig mer om hur man jobbar med tkinter. 
Ska lära mig så jag vet vad jag ska göra när jag ska skapa yatzy spelet.


24 01 19
-------------
### Tkinter

Jag hade distans hemma så jag satt och höll på och skriva på ett tre i rad spel och se lite hur man gör och försöka lära mig så jag vet vad jag ska göra sedan när jag ska skapa ett yatzy spel i tkinter.


24 01 12
-------------
### Tkinter

Jag började med att leka runt lite med tkinter i python.


23 12 18
-----------
Gjorde:
### 7080 definiera funktioner

Har skrivit kod för att räkna ut jämna och udda tal genom definitioner.

Jag har också skrivit en kod son krypterar och dekrypterar Caesarshiffer med definitioner. 

Gjorde klart alla uppgifterna så då satt jag och skrev kod för att printa ut tärningar och printa bilder.

Det känns bra att alla uppgifter är klara sista lektionen innan lovet.

Exempel:

if dots == 0:

        print(" ------- ", " ------- ", " ------- ", " ------- ", " ------- ", " ------- ")
        print("|       |", "|o      |", "|o      |", "|o     o|", "|o     o|", "|o     o|")
        print("|   o   |", "|       |", "|   o   |", "|       |", "|   o   |", "|o     o|")
        print("|       |", "|      o|", "|      o|", "|o     o|", "|o     o|", "|o     o|")
        print(" ------- ", " ------- ", " ------- ", " ------- ", " ------- ", " ------- ")


23 12 15
----------
Gjorde:
### 7080 definiera funktioner

Började skriva om def och har gjort kod för att räkna ut olika temperaturer


23 12 11
----------
Gjorde:
### 7100 listor
### Yatzy

Fortsatt på mitt yatzy spel efter jag har varit sjuk. Inte klar än.


23 12 04
----------
Gjorde:
### 7100 listor

Fortsatt på mitt yatzy spel. Har en bra bit kvar men har kommit en bra bit under denna lektion.


23 12 01
----------
Gjorde:
### 7100 listor

Blev klar med mitt BlackJack spel så nu går de att spela helt å hållet. Har öppnat en ny fil för Yatzy och börjat skriva lite grann men har inte hunnit med så mycket idag för jag blev precis klar med BlackJack. 

Exempel:

if __name__ == '__main__':

    suits = ["Spades", "Hearts", "Clubs", "Dimonds"]

    suits_values = {"Spades":"\u2664", "Hearts":"\u2661","Clubs":"\u2667", "Dimonds":"\u2662"}

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    cards_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10 }

    deck =[]



23 11 27
----------
Gjorde:
### 7100 listor

Har inprincip blivit klar med BlackJack men det finns vissa små saker jag måste fixa för att de ska funka helt å hållet.


23 11 24
---------
Gjorde:
### 7100 listor

Fortsatta att skriva på koden till BlackJack. Började också lära mig om klasser för att göra det ennklare för mig att skriva koden till BlackJack.

Exempel:

class Card:
    def __init__(self, suit, value, card_value):

    
23 11 20
------------
Gjorde:
### 7100 listor

Började att programmera jackblack

Exempel:

def blackjack_spel(kortlek):

    spelare_korten = []
    dealern_korten = []

    spelare_poäng = 0
    dealern_poäng = 0


23 11 17
------------
Gjorde:
### 7100 listor

Programmerade tärningar som skulle räknas ihop till yatzy.

Exempel:

is_yatzy = True
for tärning in tärningar:
    if t != tärning:
        is_yatzy = False

23 11 13
------------
Gjorde: 
### 7100 listor

Jag gjorde klart mina Caesarchiffer.

Exempel:

if text == 'd':
    for bokstav in text_2:
        i = svar.index(bokstav)
        i = i - 1
        if i > 28:
            i = i - 29
        if i < 0:
            i = i + 29
        meddelande += svar[i]

    print(meddelande)
    
23 11 10
-----------
Gjorde:
### 7100 listor

Jag programerade rövarspråket in i python. Sen började jag med Caesarchiffer men blev inte klar.

Exempel:

def rövarSpråkTranslator(message):
    VOWELS = ('a','e','i','o','y','å','ä','ö')
    translatedWords = []
    
23 10 27
------------
Gjorde:
### 7100 listor

Jag gjorde klart uppgift 1 och gjorde klart uppgift 2 om att skriva ut primtal

Exempel:
for i in range(2, 100):
        if is_prime(i):
            print (i)
            
23 10 23
------------
Gjorde:
### 7095 for-slingor med range
### 7096 for each-slinga
### 7100 listor

Jag har börjat lära mig hur man gör listor.

Exempel:
for i in range (10):
    tärningar.append(random.randint(1, 6))

print(tärningar)
tärningar.sort()
print("sorterad:", tärningar)
print("summa", sum(tärningar))
medel= sum(tärningar)/ len(tärningar)
print("medel:", medel)
print("min", min(tärningar))
print ("max", max(tärningar))
print("antal sexor", tärningar.count(6))


23 10 20
------------
Gjorde:
### 7073 flödesdiagram
Fil 7073 flödesdiagram.py

Jag gjorde klart koden för uppgift 6 och gjorde flödesdiagrammet och koden för uppgift 7
Exempel:
 elif (spelare_val == "sten" and dator_val == "sax") or (spelare_val == "sax" and dator_val == "påse") or (spelare_val == "påse" and dator_val == "sten"):
        spelare_poäng += 1
        print("Du fick poäng! Kör igen")
        
23 10 13
----------
Gjorde:
### 7073 flödesdiagram
Fil: 7073 flödesdiagram.py

Har gjort flödesdiagram och skrivit kod till de.
Lärt mig hur man ritar flödesdiagram

23 10 09
-----------
Gjorde:
### 7070 slumptal
Fil: 7070 slumptal.py

Exempel:
    elif tal_1 == tal_2 or tal_2 == tal_3 or tal_3 == tal_1:
        print ("minivinst")
        pengar = pengar + 5
Det gick bra
