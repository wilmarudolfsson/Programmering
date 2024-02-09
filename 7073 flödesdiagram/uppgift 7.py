import random

dator_poäng = 0
spelare_poäng = 0
val = ["sten", "sax", "påse"]

print ("Spel Sten, Sax, Påse!")

#Loopa till någon har vunnit 5 gånger
while dator_poäng < 3 and spelare_poäng < 3:
    # slumpa datorns val
    dator_val = random.choice (val)

    # låt spelare välja sten sax eller påse
    spelare_val = input("sten, sax eller påse? ")

    print("datorn valde: " + dator_val)

    # kolla vem som vann
    if dator_val == spelare_val:
        print ("Ni valde samma! Kör igen.")
    elif (spelare_val == "sten" and dator_val == "sax") or (spelare_val == "sax" and dator_val == "påse") or (spelare_val == "påse" and dator_val == "sten"):
        spelare_poäng += 1
        print("Du fick poäng! Kör igen")
    else:
        dator_poäng += 1
        print("Datorn fick poäng! Kör igen")

# säg vem som är vinnare
if dator_poäng > spelare_poäng:
    print("Datorn vann spelet!")
else:
    print("Du vann spelet! Bra jobbat!")
