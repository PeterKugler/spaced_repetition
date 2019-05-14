def make_table(table, title_list):
    table = [title_list] + table
    return table


def get_inputs(list_labels, title):
    inputs = []
    print(f"{title}")
    for item in list_labels:
        user_input = input(f"{item}")
        inputs.append(user_input)
    return inputs