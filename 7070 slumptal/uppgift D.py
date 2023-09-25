import random

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr")

svar = input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")
if svar == "i":
    svar= int(input("Ange belopp att sätta in: "))
    print("Att spela för:", svar)
svar_2 = input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")
while svar_2 == "s":
    #[1, 6)
    tal_1 = random.randrange (1, 6)
    tal_2 = random.randrange (1, 6)
    print (tal_1)
    print (tal_2)
    if tal_1 == tal_2:
        print(" två lika - vinst + 5kr")
        svar=svar + 5
        print("Att spela för: ",svar )
    elif tal_2 == tal_1 +1:
        print ("stege - vinst + 3kr")
        svar=svar + 3
        print("Att spela för: ", svar)
    elif tal_1 == 6 or tal_2 ==6:
        print ("en sexa - 3kr")
        svar=svar + 3
        print("Att spela för:", svar)
    else:
        print("förlust - 1kr")
        svar=svar - 1
        print("Att spela för",svar )
    svar_2 = input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")

   
