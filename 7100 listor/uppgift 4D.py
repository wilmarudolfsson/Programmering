text = input("Vill du kryptera eller dekryptera? Skriv k eller d: ")
text_2 = input("Skriv in ditt ord: ")
text_steg = input("Skifta antal steg: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

if text == 'k':
    for bokstav in text_2:
        i = svar.index(bokstav)
        i = i + int(text_steg)
        if i > 28:
            i = i - 29
        meddelande += svar[i]

    print(meddelande)

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