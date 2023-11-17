import random

tärningar = []
for i in range (5):
    tärningar.append(random.randint(1,6))

print (tärningar)
# för varje tärning
# om tärning är lika med föregående tärning fortsätt
# annars avbryt, inte yatzy
t = tärningar[0]
is_yatzy = True
for tärning in tärningar:
    if t != tärning:
        is_yatzy = False

if is_yatzy == True:
    print("Yatzy!!!!")
else:
    print("Ingen Yatzy")
    
