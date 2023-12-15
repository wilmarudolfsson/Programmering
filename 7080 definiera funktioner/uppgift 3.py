def kelvinToFarenheight(kelvin):
    k = kelvin
    f = (9.0/5.0) * (k-273.15) + 32
    return f

temp = float(input("Ange temperatur i grader Kelvin: "))
print("Temperaturen är", kelvinToFarenheight(temp), "Farenheight")
