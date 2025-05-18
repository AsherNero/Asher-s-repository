def shift_letter(letter, shift):
    base = ord('A') if letter.isupper() else ord('a')
    return chr((ord(letter) - base + shift) % 26 + base)

text = input("Enter the plain text: ")
shift = int(input("Enter the shift value: "))

shifted_text = ''.join(shift_letter(c, shift) if c.isalpha() else c for c in text)

print("Shifted text:", shifted_text)