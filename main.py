import sys
import user
import petproject

table = petproject.import_file("english.csv")
title_list = ["ID", "Hungarian word", "English word", "Last practiced", "Last point", "Summary of points"]


def choose():
    input = user.get_inputs(["Please enter a number: "], "")
    option = input[0]
    if option[0] == "1":
        user.print_table(table, title_list)
    elif option[0] == "2":
        petproject.create_card(table)
    elif option[0] == "3":
        petproject.remove(table)
    elif option[0] == "4":
        petproject.modify(table)
    elif option == "5":
        number_of_cards = petproject.get_number_practice_cards()
        datetime_converted = petproject.make_datetime_int(table)
        petproject.sort_practice_cards(datetime_converted)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = [
                "Look database",
                "Create card",
                "Delete card",
                "Edit card",
                "I want to practice!"]
    user.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            user.print_error_message(str(err))


if __name__ == "__main__":
    main()
