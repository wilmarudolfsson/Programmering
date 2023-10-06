import random

svar = input("Skriv j för att spela och n för att sluta: ")
while svar == "j":
    #[1, 9)
    tal_1 = random.randrange (1,9)
    tal_2 = random.randrange (1,9)
    tal_3 = random.randrange (1,9)
    print (tal_1)
    print (tal_2)
    print (tal_3)
    if tal_1 == tal_2 == tal_3:
        print ("vinst")
    elif tal_1 == 7 and tal_2 == 7 and tal_3 == 7:
        print ("dubbel vinst")
    elif tal_1 == tal_2 or tal_2 == tal_3 or tal_3 == tal_1:
        print ("minivinst")
    elif tal_1 == 7 or tal_2 == 7 or tal_3 == 7:
        print ("sjuvinst")
    else:
        print ("förlust") 
    svar = input("Skriv j för att spela och n för att sluta: ")

print("Tack för att du spelade, Välkommen åter!")