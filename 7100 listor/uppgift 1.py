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

("antal ettor", tärningar.count(1))
("antal tvåor", tärningar.count(2))
("antal treor", tärningar.count(3))
("antal fyror", tärningar.count(4))
("antal femor", tärningar.count(5))
lista = ["1", "2", "3", "4", "5", "6"]
