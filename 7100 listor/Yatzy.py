
from random import randint

def singleGame():
    roll1 = roll()
    print(format("DU SLOG: ", '64s'), roll1)
    print("")
    holdPrompt = input("BYTA UT NÅGON/NÅGRA TÄRNINGAR? (j för HITME, n för HOLD): ")
    print("")
    holdPrompt.replace(" ", "")
    holdPrompt.lower()
    while holdPrompt != "j" and holdPrompt != "n":
        print("FEL INPUT\n")
        holdPrompt = input("BYTA UT NÅGON/NÅGRA TÄRNINGAR? (j för HITME, n för HOLD):")
        print("")
        holdPrompt.replace(" ", "")
        holdPrompt.lower()
    
    if holdPrompt == "j":
        roll2 = swap(roll1)
        print("")
        print("BYTER:", roll2[1])
        print("")
        print(format("DU RULLADE: ",'64s'), roll2[0])
        print("")
        holdPrompt2 = input("BYTA UT NÅGON/NÅGRA TÄRNINGAR? (j för HITME, n för HOLD):")
        print("")
        while holdPrompt2 != "j" and holdPrompt2 != "n":
            print("FEL INPUT\n")
            holdPrompt2 = input("BYTA UT NÅGON/NÅGRA TÄRNINGAR? (j för HITME, n för HOLD):")
            print("")
            holdPrompt2.replace(" ", "")
            holdPrompt2.lower()
        if holdPrompt2 == "j":
            swapPrint = []
            roll3 = swap(roll2[0])
            print("")
            print("BYTER:", roll3[1])
            print("")
            print(format("DU RULLADE: ", '64s'), roll3[0])
            print("")
            stat = rollType(roll3[0])
        else:
            stat = rollType(roll2[0])
    elif holdPrompt == "n":
        stat = rollType(roll1)
    else:
        pass
    return stat


def roll():
    dice = []
    for x in range (5):
        dice.append(randint(1, 6))
    return dice


def swap(diceList):
    valid = True
    swapDice = input("SKRIV POSITIONEN AV TÄRNINGARNA SOM DU VILL BYTA UT (1-5): ")
    swapDice = swapDice.replace(",", "")
    swapDice = swapDice.replace(" ", "")
    swapDiceList = []
    for x in swapDice:
        swapDiceList.append(x)
    for x in swapDiceList:
        x = str(x)
        if x.isdigit():
            x = int(x)
            if x in range(1, 6):
                valid = True
            else:
                valid = False
        else:
            valid = False

    while valid == False:
        print("")
        print("FEL INPUT")
        print("")
        swapDice = input("SKRIV POSITIONEN AV TÄRNINGARNA SOM DU VILL BYTA UT (1-5): ")
        swapDice = swapDice.replace(",", "")
        swapDice = swapDice.replace(" ", "")
        swapDiceList = []
        for x in swapDice:
            swapDiceList.append(x)
        for x in swapDiceList:
            x = str(x)
            if x.isdigit():
                x = int(x)
                if x in range(1, 6):
                    valid = True
                else:
                    valid = False
            else: 
                valid = False


    swapIndex = []

    for x in swapDiceList:
        swapIndex.append(int(x)-1)

    for x in swapIndex:
        x = int(x)
        x -= 1

    for x in swapIndex:
        diceList.pop(x)
        diceList.insert(x, randint(1, 6))


    return diceList, swapDiceList

def rollType(diceList):
    counts = []
    for x in diceList:
        counts.append(diceList.count(x))
    diceListNew = sorted(diceList)
    diceListNew = list(set(diceListNew))
    yatzy = False
    kåk = False
    litenStege = False
    storStege = False
    fyrTal = False
    Triss = False
    oneCount = 0

    if 5 in counts:
        yatzy = True
        print(format("YATZY", '>80s'))
    elif 3 in counts and 2 in counts:
        kåk = True
        print(format("KÅK", '>80s'))
    elif 3 in counts and 2 not in counts:
        Triss = True
        print(format("Triss", '>80s'))
    elif 4 in counts:
        fyrTal = True
        print(format("FYRTAL", '>80s'))
    elif len(diceListNew) == 3:
        print(format("INGET SPECIELLT", '>80s'))
    elif len(diceListNew) == 4:
        if diceListNew[-2] == diceListNew[-1] -1 and diceListNew[-3] == diceListNew[-2] -1 and diceListNew[-4] == diceListNew[-3] -1:
            litenStege = True
            print(format("LITEN STEGE", '>80s'))
        else:
            print(format("INGET SPECIELLT", '>80S'))
    elif len(diceListNew) == 5:
        if diceListNew[-2] == diceListNew[-1] - 1 and diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] - 1 and diceListNew[-5] == diceListNew[-4] - 1:
            storStege = True
            print(format("STOR STEGE", '>80s'))
        elif diceListNew[-2] == diceListNew[-1] -1 and diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] - 1:
            litenStege = True
            print(format("LITEN STEGE", '>80s'))
        elif diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] -1 and diceListNew[-5] == diceListNew[-4] - 1:
            litenStege = True
            print(format("LITEN STEGE",'>80s'))
        else:
            print(format("INGET SPECIELLT", '>80s'))
    else:
        pass
    result = yatzy, kåk, litenStege, storStege, fyrTal, Triss
    return result

def main():
    yatzy = 0
    kåk = 0
    litenStege = 0
    storStege = 0 
    fyrTal = 0 
    Triss = 0
    statIndex = 0
    yatzySt = 0
    kåkSt = 0
    litenStegeSt = 0
    storStegeSt = 0
    fyrTalSt = 0
    TrissSt = 0

    print("")
    print("-" * 80)
    print("")
    print(format("VÄLKOMMEN TILL YATZY", '61s'))
    print("")
    print("-" * 80)
    print("")
    print(format("SPEL 1", '>43s'))
    print("")
    game = singleGame()
    game = list(game)
    for x in game:
       if x == True:
           statIndex = game.index(x)
    if statIndex == 0:
        yatzy += 1
    elif statIndex == 1:
        kåk += 1
    elif statIndex == 2:
        litenStege += 1
    elif statIndex == 3:
        storStege += 1
    elif statIndex == 4:
        fyrTal += 1
    elif statIndex == 5:
        Triss += 1
    else:
        pass
    print("")
    gameCount = 1
    print("SLUTET AV SPEL", gameCount)
    print("-" * 80)
    print("")
    gamesPrompt = input("SPELA EN GÅNG TILL??? (j för ja och n för nej): ")
    gamesPrompt.strip()
    gamesPrompt.lower()
    while gamesPrompt != "j" and gamesPrompt != "n":
        print("")
        print("FEL INPUT")
        print("")
        gamesPrompt = input("SPELA EN GÅNG TILL??? (j för ja och n för nej): ")
        gamesPrompt.strip()
        gamesPrompt.lower()
    print("")

    while gamesPrompt == "j":
        gameCount += 1
        print("-" * 80)
        print("")
        print(format("Spel", '>43s'), gameCount)
        print("")
        game = singleGame()
        game = list(game)
        for x in game:
            if x == True:
                statIndex = game.index(x)
        if statIndex == 0:
            yatzy += 1
        elif statIndex == 1:
            kåk += 1
        elif statIndex == 2:
            litenStege += 1
        elif statIndex == 3:
            storStege += 1
        elif statIndex == 4:
            fyrTal += 1
        elif statIndex == 5:
            Triss += 1
        else:
            pass
        print("")
        print(format("SPELET ÄR SLUT"), gameCount)
        print("-" * 80)
        print("")
        gamesPrompt = input("SPELA EN GÅNG TILL??? (j för ja och n för nej): ")
        gamesPrompt.strip()
        gamesPrompt.lower()
        while gamesPrompt != "j" and gamesPrompt != "n":
            print("")
            print("FEL INPUT")
            print("")
            gamesPrompt = input("SPELA EN GÅNG TILL??? (j för ja och n för nej): ")
            gamesPrompt.strip()
            gamesPrompt.lower()
        print("")
    if gamesPrompt == "n":
        yatzySt = (yatzy / gameCount) * 100
        kåkSt = (kåk / gameCount) * 100
        litenStegeSt = (litenStege / gameCount) * 100
        storStegeSt = (storStege / gameCount) * 100
        fyrTalSt = (fyrTal / gameCount) * 100
        TrissSt = (Triss / gameCount) * 100
        print("-"* 80)
        print("")
        print(format("STATISTIK", '>43s'))
        print("")
        print("I", gameCount, "SPEL, DU RULLADE:\n")
        if yatzy > 1 or yatzy == 0:
            print("YATZYS:", yatzy, int(yatzySt), "%")
            print("")
        else:
            print("YATZY:", yatzy, int(yatzySt), "%")
            print("")
        if kåk > 1 or kåk == 0:
            print("KÅKAR:", kåk, int(kåkSt), "%")
            print("")
        else:
            print("KÅK:", kåk, int(kåkSt), "%")
            print("")
        if litenStege > 1 or litenStege == 0:
            print("SMÅ STEGAR:", litenStege, int(litenStegeSt), "%")
            print("")
        else:
            print("LITEN STEGE:", litenStege, int(litenStegeSt), "%")
            print("")
        if storStege > 1 or storStege == 0:
            print("STORA STEGAR:", storStege, int(storStegeSt), "%")
            print("")
        else:
            print("STOR STEGE:", storStege, int(storStegeSt), "%")
            print("")
        if fyrTal > 1 or fyrTal == 0:
            print("FYRTAL:", fyrTal, int(fyrTalSt), "%")
            print("")
        else:
            print("FYRTAL:", fyrTal, int(fyrTalSt), "%")
            print("")
        if Triss > 1 or Triss == 0:
            print("TRISSAR:", Triss, int(TrissSt), "%")
            print("")
        else:
            print("TRISS:", Triss, int(TrissSt), "%")
            print("")


main()
