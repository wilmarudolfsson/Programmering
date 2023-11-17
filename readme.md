Loggbok
===========
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
