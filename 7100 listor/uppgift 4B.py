text = input("Mata in ett ord att dekryptera: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

for bokstav in text:
    i = svar.index(bokstav)
    i = i - 1
    if i > 28:
        i = i - 29
    if i < 0:
        i = i + 29
    meddelande += svar[i]

print(meddelande)