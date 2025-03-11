alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
direction = input("choose 'encode' to encrypt and 'decode' to decrypt")
user_input = input("enter your message").upper()
shift = int(input("enter the shift number"))

def encode(msg,num):
    cipher_text = ""
    for i in msg:
        current_position = alphabet.index(i)
        shifted_position = current_position+num
        new_letter = alphabet[shifted_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")



def decode(msg,num):
    cipher_text = ""
    for i in msg:
        current_position = alphabet.index(i)
        shifted_position = current_position-num
        new_letter = alphabet[shifted_position]
        cipher_text += new_letter
    print(f"the decoded text is {cipher_text}")



if direction == 'encode':
    encode(msg=user_input, num=shift)
if direction == 'decode':
    decode(msg=user_input, num=shift)

