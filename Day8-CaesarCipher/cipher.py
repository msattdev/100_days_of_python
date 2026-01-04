# Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
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

# decrypt(original_text=text, shift_amount=shift)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            if encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            elif encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"The {encode_or_decode}d text is: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)