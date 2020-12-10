from functools import reduce
from operator import mul
import numpy as np

IN_FILE = 'day10-input.txt'


def get_input(in_file: str) -> list:
    with open(in_file) as f:
        lines = [int(x.replace('\n', '')) for x in f.readlines()]
    lines = sorted(lines)
    lines = [0] + lines + [lines[-1]+3]
    return sorted(lines)


def chain_differences(adapters: list) -> (int, int):
    diff_1, diff_3 = 0, 0
    for i in range(0, len(adapters)-1):
        cur_voltage = adapters[i]
        diff = adapters[i+1] - cur_voltage
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        else:
            print("Invalid Difference: {} not in range(1, 3)".format(diff))
            raise ValueError
    return diff_1, diff_3


def get_all_unique_sequences_count(adapters: list) -> list:
    diff = np.array(np.diff(adapters))

    skips = list(map(len, ''.join('-' if x == 1 else '*' for x in diff).split('*')))
    translate = [1, 1, 2, 4, 7]

    return reduce(mul, map(lambda x: translate[x], skips))


def main():
    adapters = get_input(IN_FILE)
    diff_1, diff_3 = chain_differences(adapters)
    print("Part 1:\n\tDifferences of 1 * Differences of 2:\n\t\t{}".format(diff_1*diff_3))

    diff_sequences = get_all_unique_sequences_count(adapters)
    print("Part 2:\n\tTotal amount of unique adapter configurations:\n\t\t{}".format(diff_sequences))


if __name__ == '__main__':
    main()
