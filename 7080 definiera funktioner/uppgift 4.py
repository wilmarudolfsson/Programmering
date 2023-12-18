temperatur_skala = {
    'Celsius': 'C',
    'Farenheight': 'F',
    'Kelvin': 'K'
}

def convert_tempertures(value, input_skala, output_skala):
    if input_skala == 'C':
        if output_skala == 'F':
            return value * 1.8 + 32
        elif output_skala == 'K':
            return value + 273.15
        else:
            return value
    elif input_skala == 'F':
        if output_skala == 'C':
            return (value - 32) / 1.8
        elif output_skala == 'K':
            return (value - 459.67) * (5.0/9.0)
        else:
            return value
    elif input_skala == 'K':
        if output_skala == 'C':
            return value -273.15
        elif output_skala == 'F':
            return value *(9.0/5.0) - 459.67
        else:
            return value
    else:
        return value
    
while True:
    print("Ange ingångstemperaturens värde: ")
    value = float(input())
    print("Skriv in ingångstempraturdskalan (C, F eller K): ")
    input_skala = input().upper()
    print("Ange utgångstemperaturensskalan (C, F eller K): ")
    output_skala = input().upper()

    resultat = convert_tempertures(value, input_skala, output_skala)
    print(f'{value} {input_skala} = {resultat} {output_skala}')

    print("Skriv s för att sluta, eller vilken kanpp som helst för att fortsätta: ")
    choise = input()
    if choise.lower() == 's':
        break
    

        

        

        