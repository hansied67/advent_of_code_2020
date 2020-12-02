import re

IN_FILE = 'day2-input.txt'
VALID_PASS_REGEX = r'^([\d]+)-([\d]+) ([A-Za-z]): ([A-Za-z]+)$'


# returns each line from the input file as a string in an array
def get_input():
    f = open(IN_FILE, 'r')
    in_list = f.readlines()
    f.close()
    return [x.replace('\n', '') for x in in_list]


def get_capture(toboggan_pass):
    return re.search(VALID_PASS_REGEX, toboggan_pass)


def is_pass_valid(toboggan_pass_regex):
    lower_bound = int(toboggan_pass_regex.group(1))
    upper_bound = int(toboggan_pass_regex.group(2))
    desired_char = toboggan_pass_regex.group(3)
    pass_to_check = toboggan_pass_regex.group(4)

    char_count = pass_to_check.count(desired_char)

    return lower_bound <= char_count <= upper_bound


def is_pass_valid_part2(toboggan_pass_regex):
    lower_index = int(toboggan_pass_regex.group(1)) - 1
    upper_index = int(toboggan_pass_regex.group(2)) - 1
    desired_char = toboggan_pass_regex.group(3)
    pass_to_check = toboggan_pass_regex.group(4)

    lower_check = pass_to_check[lower_index] == desired_char
    upper_check = pass_to_check[upper_index] == desired_char

    return lower_check != upper_check


def main():
    pass_list = get_input()

    print("---PART 1---")
    valid_passwords = 0
    for user_pass in pass_list:
        capture = get_capture(user_pass)
        if is_pass_valid(capture):
            valid_passwords = valid_passwords + 1
        else:
            print("Invalid password:\t{}".format(user_pass))

    solution_1 = "There are {} valid matches and {} invalid matches.".format(
        valid_passwords, len(pass_list)-valid_passwords)

    # -----------------------------------------------------------
    print("---PART 2---")
    valid_passwords = 0
    for user_pass in pass_list:
        capture = get_capture(user_pass)
        if is_pass_valid_part2(capture):
            valid_passwords = valid_passwords + 1
        else:
            print("Invalid password:\t{}".format(user_pass))

    solution_2 = "There are {} valid matches and {} invalid matches.".format(
        valid_passwords, len(pass_list)-valid_passwords)

    print("Part 1: \n\t{}".format(solution_1))
    print("Part 2: \n\t{}".format(solution_2))


if __name__ == '__main__':
    main()
