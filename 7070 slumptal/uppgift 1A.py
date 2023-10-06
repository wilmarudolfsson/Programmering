
import random

svar=input("Vill du spela? ja/nej " )
while svar == "ja":
   
    #[1, 6)
    tal_1 = random.randrange(1, 6)
    tal_2 = random.randrange(1, 6)
    print (tal_1)
    print (tal_2)
    if tal_1 == tal_2:
        print ("vinst")
    else: 
        print ("förlust")
    svar=input("Vill du spela igen? ja/nej " )

print ("Vad roligt att du spelade en stund!")