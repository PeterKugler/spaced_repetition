def make_table(table, title_list):
    table = [title_list] + table
    return table


def transform_table(table):
    for row in table:
        for i in range(len(row)):
            if type(row[i]) == int:
                row[i] = str(row[i])
    new_table = list(zip(*table))
    return new_table


def len_of_table(new_table):
    length_of_table = len(new_table[0])
    return length_of_table


def len_of_columns(new_table):
    length_of_items = []
    for lists in new_table:
        for item in lists:
            length_of_items.append(len(item))
            


def print_table(table, title_list):
    table = make_table(table, title_list)
    new_table = transform_table(table)
    dash_chr = "="
    right_slash = "/"
    left_slash = "\"
    separator = "||"

    