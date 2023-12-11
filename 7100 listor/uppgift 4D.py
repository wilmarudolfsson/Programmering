'''text = input("Vill du kryptera eller dekryptera? Skriv k eller d: ")
text_2 = input("Skriv in ditt ord: ")
text_steg = input("Skifta antal steg: ")

svar = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = ""

if text == 'k':
    for bokstav in text_2:
        i = svar.index(bokstav)
        i = i + int(text_steg)
        if i > 28:
            i = i - 29
        meddelande += svar[i]

    print(meddelande)

if text == 'd':
    for bokstav in text_2:
        i = svar.index(bokstav)
        i = i - 1
        if i > 28:
            i = i - 29
        if i < 0:
            i = i + 29
        meddelande += svar[i]

    print(meddelande)'''


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")