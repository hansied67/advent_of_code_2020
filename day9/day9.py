IN_FILE = 'day9-input.txt'
from copy import deepcopy


def get_input(in_file: str) -> (list, list):
    with open(in_file) as f:
        lines = [int(x.replace('\n', '')) for x in f.readlines()]
        preamble = lines[:25]
        sums = lines[25:]
        return preamble, sums


def get_possible_sums(preamble: list) -> list:
    possible_sums = list()
    for i, _num in enumerate(preamble):
        for x in preamble[(i+1):]:
            possible_sums.append(_num+x)
    return possible_sums


def update_sums_and_preamble(preamble: list, cur_num: int) -> (list, list):
    preamble_temp = deepcopy(preamble[1:])
    preamble_temp.append(cur_num)

    sums_temp = get_possible_sums(preamble_temp)

    return preamble_temp, sums_temp


def main():
    preamble, sums = get_input(IN_FILE)
    possible_sums = get_possible_sums(preamble)

    broken_sum = -1
    for i, _sum in enumerate(sums):
        if _sum not in possible_sums:
            broken_sum = _sum
            break
        if (i+1) == len(sums):
            print('all good')
        else:
            preamble, possible_sums = update_sums_and_preamble(preamble, _sum)
    print(broken_sum)

    sum_range_fix = -1
    for i in range(len(sums)):
        for j in range(i + 2, len(sums)):
            considering = sums[i:j]
            total = sum(considering)
            if total == broken_sum:
                sum_range_fix = sum(sorted(considering)[::len(considering) - 1])
                break
        if sum_range_fix != -1:
            break
    print(sum_range_fix)




if __name__ == '__main__':
    main()