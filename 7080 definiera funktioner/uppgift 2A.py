def celsiusToFarenheight(celsius):
    C = celsius
    F = (9.0/5.0) * C + 32
    return F

temp = float(input("Ange temperatur i grader Celsius: "))
print("Temperaturen är", celsiusToFarenheight(temp), "Farenheight")
