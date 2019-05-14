import random


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
    