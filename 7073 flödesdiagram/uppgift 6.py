svar=int(input("Gissa på ett tal:"))
antal_gissningar = 1
while svar !=42 and antal_gissningar == antal_gissningar:
    if svar < 42:
        print("För litet, Gissa igen")
    else:
        print("För stort, Gissa igen")
    svar=int(input("Gissa på ett tal:"))
    antal_gissningar = antal_gissningar + 1
print("Det tog dig", antal_gissningar ,"gissningar att få rätt svar!")