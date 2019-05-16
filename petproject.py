import random
import user
import datetime
from operator import itemgetter


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


def create_card(table):
    list_labels = ["word in Hungarian ", "word in foreign language "]
    title = "add word(s) to list"
    last_point = 0
    sum_of_points = 0
    inputs = user.get_inputs(list_labels, title)
    randomised_key = generate_random(table)
    inputs.insert(0, str(randomised_key))
    current_datetime = datetime.datetime.today()
    cd_string = datetime.datetime.strftime(current_datetime, "%d/%m/%Y, %H:%M")
    inputs.append(cd_string)
    inputs.append(str(last_point))
    inputs.append(str(sum_of_points))
    table.append(inputs)
    writer = export_file("english.csv", table)
    return table


def remove(table):
    id_to_remove = input("Enter ID of word to remove: ")
    for row in table:
        if id_to_remove in row:
            table.remove(row)
    writer = export_file("english.csv", table)
    return table


def modify(table):
    list_labels = ["word in Hungarian ", "Word in foreign language "]
    id_to_update = input("Enter ID of word to update ")
    for row in table:
        if id_to_update in row:
            table.remove(row)
            inputs = user.get_inputs(list_labels, "Changing from/to")
            row[1] = inputs[0]
            row[2] = inputs[1]
            table.append(row)
    writer = export_file("english.csv", table)
    return table


def get_number_practice_cards():
    valid_number = False
    while valid_number is False:
        try:
            number_to_practice = int(input("How many cars would you like to practice? "))
            valid_number = True
        except ValueError:
            print("Please give a valid integer number!")
    return number_to_practice


def make_datetime_int(table):
    DATETIME = 3
    make_datetime = []
    for word in table:
        chars_to_replace = "/,: "
        datetime_formatted = ""
        for char in word[DATETIME]:
            if char in chars_to_replace:
                datetime_formatted += char.replace(char, "")
            else:
                datetime_formatted += char
        word.remove(word[DATETIME])
        word.insert(DATETIME, datetime_formatted)
        make_datetime.append(word)
    return make_datetime


def sort_practice_cards(table, number_of_cards):
    table.sort(key=itemgetter(4, 3, 5))
    table = table[:number_of_cards + 1]
    return print(table)