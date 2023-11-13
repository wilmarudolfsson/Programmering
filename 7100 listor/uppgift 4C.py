text = input("Mata in ord: ")
text_steg = input("Skifta antal steg: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

for bokstav in text:
    i = svar.index(bokstav)
    i = i + int(text_steg)
    if i> 28:
        i = i - 29
    meddelande += svar[i]

print(meddelande)