import random

tärningar = []
for i in range (5):
    tärningar.append(random.randint(1,6))

print (tärningar)
print ("antal ettor", tärningar.count(1))
