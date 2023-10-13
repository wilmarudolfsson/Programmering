svar = input("Skriv in ett tal: ")
if svar == (0, 9):
    print (svar, "är ett ensiffrigt tal")
elif svar == 10 <= 99:
    print (svar, "är ett tvåsiffrigt tal")
elif svar == 100 <= 999:
    print (svar, "är ett tresiffrigt tal")
elif svar == 'svar' < 0:
    print(svar, "är ett negativt tal")
else:
    print (svar, "är minst ett fyrsiffrigt tal")