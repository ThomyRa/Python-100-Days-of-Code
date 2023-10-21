alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def encrypt(input_text, shift_number):
    new_text = ''
    for char in input_text:
        new_idx = alphabet.index(char)
        if (new_idx + shift_number) > (len(alphabet) - 1):
            new_text += alphabet[shift_number - 1]
        else:
            new_text += alphabet[new_idx + shift_number]

    print(f'The encoded text is: {new_text}')


def decrypt(encrypted_text, shift_number):
    original_text = ''
    for char in encrypted_text:
        original_idx = alphabet.index(char)
        original_text += alphabet[original_idx - shift_number]

    print(f'The decoded text is {original_text}')

if direction == 'encode':
    encrypt(input_text = text, shift_number = shift)
elif direction == 'decode':
    decrypt(encrypted_text = text, shift_number = shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(input_text, shift_number, direction):
    new_text = ''
    for char in input_text:
        original_idx = alphabet.index(char)
        if (direction == 'encode') :
            if (original_idx + shift_number > len(alphabet) - 1):
                new_text += alphabet[shift_number - 1]
            else:
                new_text += alphabet[original_idx + shift_number]
        elif (direction == 'decode'):
            new_text += alphabet[original_idx - shift_number]
    print(f'The {direction}d text is: {new_text}')

caesar(text, shift, direction)
