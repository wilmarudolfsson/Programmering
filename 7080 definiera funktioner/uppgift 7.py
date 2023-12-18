alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

def caesar(start_text, shift_amount, cipher_direction):
  slut_text = ""
  print(cipher_direction + "_")
  if cipher_direction == "d":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      ny_position = position + shift_amount
      slut_text += alphabet[ny_position]
    else:
      slut_text += char
  print(f"Här är resultat: {slut_text}")


should_end = False
while not should_end:

  direction = input("Skriv 'k' för att kryptera, Skriv 'd' för att dekryptera:\n")
  text = input("Skriv ditt meddelande:\n").lower()
  shift = int(input("Skriv antal steg som ska shifta:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Skriv 'ja' om du vill göra det igen, annars skriv 'nej'.\n")
  if restart == "nej":
    should_end = True
    print("Hejdå")