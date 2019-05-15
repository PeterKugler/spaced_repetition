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
def add_word(table):
    list_labels = ["word in foreign language", "word in Hungarian", "date of first practice"]
    title = "add word(s) to list"
    inputs = user.get_inputs(list_labels, title)
    randomised_key = generate_random(table)
    inputs.insert(0, str(randomised_key))
    #todo: append list with points. Table needed for sequence