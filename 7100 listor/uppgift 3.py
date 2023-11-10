
import sys

def rövarSpråkTranslator(message):
    VOWELS = ('a','e','i','o','y','å','ä','ö')
    translatedWords = []

    for word in message.split():
        if not word.isalpha():
            continue

        translatedWord = ''

        while len(word) > 0:
            if word[0].lower() not in VOWELS:
                if word[0].lower() == 'x':
                    word = 'k'
                    word = 's' + word
                if word[0].isupper():
                    translatedWord += word[0]
                else:
                    translatedWord += word[0].lower()
                translatedWord += 'o' + word[0].lower()
            else:
                if word[0].isupper:
                    translatedWord += word[0]
                else: 
                    translatedWord += word[0].lower()
            word = word[1:] 

        translatedWords.append(translatedWord) 

    return ' '.join(translatedWords) 

if len(sys.argv) == 2: 
    print(rövarSpråkTranslator(sys.argv[1]))
    sys.exit()
elif len(sys.argv) > 2: 
    print("Usage: python rövarSpråk.py [str]")
else:
    message = input('Mata in ett ord/mening som blir översatt till Rövarspråk: ') 
    translatedMessage = rövarSpråkTranslator(message)
    print(translatedMessage)