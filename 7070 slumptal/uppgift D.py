import random

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr")

svar = input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")
if svar == "i":
    svar= input("Ange belopp att sätta in: ")
    print("Att spela för:", svar)
svar_2 = input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")
while svar_2 == "s":
    #[1, 6)
    tal_1 = random.randrange (1, 6)
    tal_2 = random.randrange (1, 6)
    if tal_1 == tal_2:
        print(" två lika-vinst + 5kr")
        input("Att spela för: ",svar + 5)
    else:
        print("förlust")
        input("Att spela för", svar--1)
    


