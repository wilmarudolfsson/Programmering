def farenheightToCelsius(farenheight):
    F = farenheight
    C = (5.0/9.0) * (F-32)
    return C

temp = float(input("Ange temperatur i grader Farenheight: "))
print("Temperaturen är", farenheightToCelsius(temp), "Celsius")
