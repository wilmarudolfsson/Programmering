def kelvinToCelsius(Kelvin):
    return Kelvin - 273.15

temp = float(input("Ange temperatur i grader Kelvin: "))
print("Temperaturen är", kelvinToCelsius(temp), "Celsius")
