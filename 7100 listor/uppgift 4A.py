text = input("Mata in ord: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

for bokstav in text:
    i = svar.index(bokstav)
    # om i + 1 är för mycket, mer än 28 -> flytta 29 steg åt vänster
    # max i är ca 28
    #print(svar.index("ö"))
    i = i + 1
    if i> 28:
        i = i - 29
    meddelande += svar[i]

print(meddelande)
    
'''
for bokstav in text: 
    kod = ord(bokstav)
    kod = kod + 1
    if kod > 122:
        # för mycket
        kod = kod - 26
    ny_bokstav=chr(kod)
    meddelande += ny_bokstav
print(meddelande)'''




