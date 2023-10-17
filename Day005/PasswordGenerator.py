import random

def random_letter(letters):
    letter_idx = random.randint(0, len(letters) - 1)
    return letters[letter_idx]

def random_number(numbers):
    number_idx = random.randint(0, len(numbers) - 1)
    return numbers[number_idx]

def random_symbol(symbols):
    symbol_idx = random.randint(0, len(symbols) - 1)
    return symbols[symbol_idx]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for _ in range(nr_letters):
    password += random_letter(letters)

for _ in range(nr_numbers):
    password += random_number(numbers)

for _ in range(nr_symbols):
    password += random_symbol(symbols)


password = list(password)
random.shuffle(password)

shuffled_pass = ''
for _ in password:
    shuffled_pass += _

print(shuffled_pass)
