svar = int(input("Skriv in ett tal: "))
if 0 <= svar and svar <= 9:
    print (svar, "är ett ensiffrigt tal")
elif 10 <= svar and svar <= 99:
    print (svar, "är ett tvåsiffrigt tal")
elif 100 <= svar and svar <= 999:
    print (svar, "är ett tresiffrigt tal")
elif svar <= -1:
    print(svar, "är ett negativt tal")
else:
    print (svar, "är minst ett fyrsiffrigt tal")