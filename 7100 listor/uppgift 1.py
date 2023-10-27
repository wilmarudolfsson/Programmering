import random

tärningar = []

for i in range (10):
    tärningar.append(random.randint(1, 6))

print(tärningar)
tärningar.sort()
print("sorterad:", tärningar)
print("summa", sum(tärningar))
medel= sum(tärningar)/ len(tärningar)
print("medel:", medel)
print("min", min(tärningar))
print ("max", max(tärningar))
print("antal sexor", tärningar.count(6))

antal = [0]
for i in range(1, 7):
    antal.append(tärningar.count(i))

lista = ["1", "2", "3", "4", "5", "6"]

maximum = max(antal)
vanligaste_tärningen = antal.index(maximum)

print("Vanligaste valör: ",vanligaste_tärningen)




