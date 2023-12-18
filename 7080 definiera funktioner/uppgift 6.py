def jämnEllerUdda(a):
    if a % 2 == 0:
        return 'Jämnt tal'
    else:
        return 'Udda tal'
    
Tal = int(input("Skriv in ett positivt heltal: "))
print(jämnEllerUdda(Tal))


