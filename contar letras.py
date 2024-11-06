def letter_count(text, letter):
    contador = 0
    for caracter in text:
        if caracter.lower() == letter.lower():
            contador += 1
    return contador

text = input()
letter = input()

print(letter_count(text, letter))