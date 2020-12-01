from itertools import combinations

IN_FILE = 'day1-input.txt'
FIRST_TUPLE_SIZE = 2
SECOND_TUPLE_SIZE = 3
DESIRED_SUM = 2020


# returns input list from part 1
def get_input():
    f = open(IN_FILE, 'r')
    in_list_part1 = f.readlines()
    f.close()
    return [int(x.replace('\n', '')) for x in in_list_part1]


# returns tuple: tuple[0] is the valid pair, tuple[1] is the product.
def get_expense_pair_and_product(expenses, r):
    all_tuples = list(combinations(expenses, r))
    valid_tuple = [pair for pair in all_tuples if sum(pair) == DESIRED_SUM][0]

    product = 1
    for expense in valid_tuple:
        product = product * expense

    return valid_tuple, product


def print_solution(valid_tuple, product):
    valid_tuple_str_rep = [str(x) for x in valid_tuple]
    addition_expression = '{} = {}'.format(' + '.join(valid_tuple_str_rep), str(sum(valid_tuple)))
    multiplication_expression = '{} = {}'.format(' * '.join(valid_tuple_str_rep), product)

    print("Solution:")
    print('\t{}\n\t{}'.format(addition_expression, multiplication_expression))


def main():
    input_list = get_input()
    part1_solution = get_expense_pair_and_product(input_list, FIRST_TUPLE_SIZE)
    part2_solution = get_expense_pair_and_product(input_list, SECOND_TUPLE_SIZE)

    print_solution(part1_solution[0], part1_solution[1])
    print_solution(part2_solution[0], part2_solution[1])


if __name__ == '__main__':
    main()
