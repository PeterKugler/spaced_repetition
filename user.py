def make_table(table, title_list):
    table = [title_list] + table
    return table


def transform_table(table):
    for row in table:
        for i in range(len(row)):
            if type(row[i]) == int:
                row[i] = str(row[i])
    new_table = list(zip(*table))
    print(new_table)
    return new_table


def len_of_table(new_table):
    length_of_table = len(new_table[0])
    return length_of_table


def len_of_columns(new_table):
    length_of_items = []

    for lists in new_table:
        for item in lists:
            length_of_items.append(len(item))

    length_of_table = len_of_table(new_table)
    row_to_column_list = [length_of_items[x:x+length_of_table] for x in range(0, len(length_of_items), length_of_table)]
    longest_titles = []
    
    for i in row_to_column_list:
        longest_titles.append(max(i))
    print(longest_titles)
    
    count = 0
    for i in longest_titles:
        design_width = 5
        longest_titles[count] += design_width
        count += 1
    return longest_titles


def print_table(table, title_list):
    table = make_table(table, title_list)
    new_table = transform_table(table)
    dash_chr = "="
    right_slash = "/"
    left_slash = "\\"
    separator = "||"

    longest_titles = len_of_columns(new_table)
    separator_line = []

    for i in longest_titles:
        separator_line.append(i*dash_chr+separator)

    joint_separator_line = "".join(separator_line)
    list_separator_line = separator + joint_separator_line
    last_line = left_slash + (len(joint_separator_line)-1)*dash_chr+right_slash
    first_line = right_slash + (len(joint_separator_line)-1)*dash_chr+left_slash
    print(first_line)

    for lists in table:
        if lists == table[0]:
            pass
        else:
            print(f"\n{list_separator_line}")
        print(end=separator)
        print(separator, end="")

    for enum, item in enumerate(lists):
        print(item.center(longest_titles[enum]), end=separator)

    print("")
    print(last_line)
    #return table, title_list


def print_result(result, label):
    if type(result) == list:
        print(label)
        print(result)
        print("")
    elif type(result) == dict:
        print(label)
        for key, value in result.items():
            print(key, value)
            print("")
    else:
        print(label)
        print(result)
        print("")


def print_menu(title, list_options, exit_message):
    print(f'\t{title}:')
    for i in range(len(list_options)):
        print(f'\t\t({i+1}) {list_options[i]}')
    print(f'\t\t(0) {exit_message}')


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for list_label in list_labels:
        user_input = input(list_label)
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    print('Error: ' + message)
