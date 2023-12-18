def show_die(dots):
    if dots == 0:
        print(" ------- ", " ------- ", " ------- ", " ------- ", " ------- ", " ------- ")
        print("|       |", "|o      |", "|o      |", "|o     o|", "|o     o|", "|o     o|")
        print("|   o   |", "|       |", "|   o   |", "|       |", "|   o   |", "|o     o|")
        print("|       |", "|      o|", "|      o|", "|o     o|", "|o     o|", "|o     o|")
        print(" ------- ", " ------- ", " ------- ", " ------- ", " ------- ", " ------- ")
    elif dots == 1:
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
    elif dots == 2:
        print(" ------- ")
        print("|o      |")
        print("|       |")
        print("|      o|")
        print(" ------- ")
    elif dots == 3:
        print(" ------- ")
        print("|o      |")
        print("|   o   |")
        print("|      o|")
        print(" ------- ")
    elif dots == 4:
        print(" ------- ")
        print("|o     o|")
        print("|       |")
        print("|o     o|")
        print(" ------- ")
    elif dots == 5:
        print(" ------- ")
        print("|o     o|")
        print("|   o   |")
        print("|o     o|")
        print(" ------- ")
    elif dots == 6:
        print(" ------- ")
        print("|o     o|")
        print("|o     o|")
        print("|o     o|")
        print(" ------- ")

show_die(1)
show_die(2)
show_die(3)
show_die(4)
show_die(5)
show_die(6)
show_die(0)


