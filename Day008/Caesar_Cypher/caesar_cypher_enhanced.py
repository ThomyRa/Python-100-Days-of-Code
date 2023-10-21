import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(input_text, shift_number, cypher_direction):
    new_text = ''

    if shift_number > len(alphabet):
        shift_number = shift_number % len(alphabet)

    for char in input_text:
        if char in alphabet:
            original_idx = alphabet.index(char)
            shift_idx = len(alphabet) - 1 + shift_number
            if (direction == 'encode') :
                if (original_idx + shift_number) > (len(alphabet) - 1):
                    new_text += alphabet[shift_number - (len(alphabet) - original_idx)]
                else:
                    new_text += alphabet[original_idx + shift_number]
            elif (direction == 'decode'):
                new_text += alphabet[original_idx - shift_number]
        else:
            new_text += char
    print(f'The {direction}d text is: {new_text}')

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text = text, shift_number = shift, cypher_direction = direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if choice == 'no':
        break
