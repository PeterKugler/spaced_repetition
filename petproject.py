import random
import user


def import_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def export_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def generate_random_letter(letter1, letter2):
    return chr(random.randint(ord(letter1), ord(letter2)))


def generate_random(table):
    generated = ''

    while generated == '':
        for i in range(2):
            generated += generate_random_letter("a", "z")
            generated += generate_random_letter("A", "Z")
            generated += generate_random_letter("0", "9")
            generated += generate_random_letter("!", "/")

        if generated not in table:
            return generated
        else:
            generated = ''
            continue

# CRUD


def create_card(table):
    list_labels = ["word in Hungarian", "word in foreign language"]
    title = "add word(s) to list"
    last_point = 0
    sum_of_points = 0
    inputs = user.get_inputs(list_labels, title)
    randomised_key = generate_random(table)
    inputs.insert(0, str(randomised_key))
    inputs.append(str(last_point), str(sum_of_points))  # todo: append the list of values with time as well
    table.append(inputs)
    # todo: write the updated table to file


def remove(table):
    id_to_remove = input("Enter ID of word to remove: ")
    for row in table:
        if id_to_remove in table:
            table.remove(row)
    # todo: write the updated table to file


def modify(table):
    list_labels = ["word in Hungarian", "Word in foreign language"]
    id_to_update = input("Enter ID of word to udate")
    for row in table:
        if id_to_update == row[0]:
            row = [id_to_update] + user.get_inputs(list_labels, "Changing from/to") + row[-3:-1]
    # todo: write the updated table to file