def find_max(number_set):
    max_val = number_set[0]
    for number in number_set:
        if number > max_val:
            max_val = number
