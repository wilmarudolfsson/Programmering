import random

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr")

svar= input ("Välj spela (s), sätt in pengar (i), eller avsluta (a):")
if svar== "i":
    input("Ange belopp att sätta in: ")
svar_2=svar
if svar_2:
    print("Att spela för:",svar_2)
