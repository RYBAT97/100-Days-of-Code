with open("Input/Letters/starting_letter.txt") as file:
    default_letter = file.read()

names_list = []
with open("Input/Names/invited_names.txt", mode='r') as file:
    names = file.readlines()
    for item in names:
        names_list.append(item.rstrip())

for name in names_list:
    new_letter = default_letter
    new_letter = new_letter.replace('[name]', name)
    new_file = open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w')
    new_file.write(new_letter)
    new_file.close()
