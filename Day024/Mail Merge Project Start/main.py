
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    all_names = file.readlines()
all_names = [name.strip() for name in all_names]

for name in all_names:
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
        starting_letter = file.readlines()
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.txt", "w") as file:
        starting_letter[0] = starting_letter[0].replace("[name]", name)
        print(starting_letter[0])
        file.writelines(starting_letter)
