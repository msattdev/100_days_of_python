# Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"The encoded text is: {cipher_text}")

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        original_position = alphabet.index(letter) - shift_amount
        original_position %= len(alphabet)
        decoded_text += alphabet[original_position]
    print(f"The decoded text is: {decoded_text}")

decrypt(original_text=text, shift_amount=shift)