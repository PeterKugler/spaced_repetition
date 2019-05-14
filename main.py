import sys

def choose():
    input = get_user_input(["Please enter a number: "], "")
    option = input[0]
    if option[0] == "1":
        look_database(table)
    elif option[0] == "2":
        cards = create_card(card)
    elif option[0] == "3":
        table = remove(table, card[0])
    elif option[0] == "4":
        table = modify(table, card[0])
    elif option == "5":
        input = get_user_input(["How many cards woul you like? "], "")
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Look database",
                "Create card",
                "Delete card",
                "Edit card",
                "I want to practice!"]
    print_menu


def main():
    while True:
        handle_menu()
        try:
            choose()
        except:
            raise KeyError


if __name__ == "__main__":
    main()
