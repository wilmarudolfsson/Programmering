text = input("Mata in ord: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

for bokstav in text:
    i = svar.index(bokstav)
    # om i + 1 är för mycket -> flytta 29 steg åt vänster
    meddelande += svar[i+1]
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




