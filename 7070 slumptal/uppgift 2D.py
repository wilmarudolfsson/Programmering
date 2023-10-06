import random

pengar = 100
svar = input("Skriv j för att spela och n för att sluta: ")
while svar == "j":

    print("kvar att spela för:", pengar, "kronor")
    #[1, 9)
    tal_1 = random.randrange (1,9)
    tal_2 = random.randrange (1,9)
    tal_3 = random.randrange (1,9)
    print (tal_1)
    print (tal_2)
    print (tal_3)
    if tal_1 == tal_2 == tal_3:
        print ("vinst")
        pengar = pengar + 25
        print ("Kvar att spela för:", pengar, "kronor")
    elif tal_1 == 7 and tal_2 == 7 and tal_3 == 7:
        print ("dubbel vinst")
        pengar = pengar + 50
        print ("Kvar att spela för:", pengar, "kronor")
    elif tal_1 == tal_2 or tal_2 == tal_3 or tal_3 == tal_1:
        print ("minivinst")
        pengar = pengar + 5
        print ("Kvar att spela för:", pengar, "kronor")
    elif tal_1 == 7 or tal_2 == 7 or tal_3 == 7:
        print ("sjuvinst")
        pengar = pengar + 2
        print ("Kvar att spela för:", pengar, "kronor")
    else:
        print ("förlust") 
        pengar = pengar - 1
        print ("Kvar att spela för:", pengar, "kronor")
    svar = input("Spela mer? j/n: ")

print("Tack för att du spelade, Välkommen åter!")