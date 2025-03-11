print("Welcome soldiers! This is to save you from your enemies!")
alphabet = ['a', 'b', 'c', 'd', '.............................']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt")
original_message = input("Type your message")
shift = int(input("Enter the shift number"))


def ceaser(original_text, shift_number, encode_or_decode):
    cipher = " "
    for letter in original_text:
        if encode_or_decode == 'decode':
            shift_number *= -1
        shifted_position = alphabet.index(letter) + shift_number
        shifted_position %= len(alphabet)
        cipher += letter(shifted_position)
    print(f"here is the {encode_or_decode}d result: {cipher}")


ceaser(original_text=original_message, shift_number=shift, encode_or_decode=direction)
