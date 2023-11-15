
with open("./Input/Names/invited_names.txt") as file:
    all_names = file.readlines()
all_names = [name.strip() for name in all_names]

for name in all_names:
    with open("./Input/Letters/starting_letter.txt") as file:
        starting_letter = file.readlines()
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
        starting_letter[0] = starting_letter[0].replace("[name]", name)
        file.writelines(starting_letter)
