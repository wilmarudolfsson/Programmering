import random

svar=input("Vill du spela? ja/nej " )
while svar == "ja":
   
    #[1, 6)
    tal_1 = random.randrange(1, 7)
    tal_2 = random.randrange(1, 7)
    print (tal_1)
    print (tal_2)
    if tal_1 == 6 or tal_2 == 6:
        print ("vinst")
    else: 
        print ("förlust")
    svar=input("Vill du spela igen? ja/nej " )

print ("Vad roligt att du spelade en stund!")