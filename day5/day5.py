import re

IN_FILE = 'day5-input.txt'


class BoardingPassEntry(object):

    ROWS = list(range(128))
    COLUMNS = list(range(8))
    ID_SCALING = 8

    BSP_REGEX = r'^([FB]{7})([LR]{3})$'
    FRONT = BSP_REGEX[3]
    BACK = BSP_REGEX[4]
    LEFT = BSP_REGEX[12]
    RIGHT = BSP_REGEX[13]

    def __init__(self, entry: str, *args):
        regex = self.BSP_REGEX
        if len(args) == 1:
            regex = args[0]
        elif len(args) > 1:
            raise ValueError

        self._capture = re.match(regex, entry)
        if self._capture is None:
            raise ValueError

        self._id = self._calc_id()

    def _calc_id(self) -> tuple:
        row = self.ROWS
        for pos in self._capture.group(1):
            half_point = (len(row) + 1) // 2
            if pos == self.FRONT:
                row = row[:half_point]
            elif pos == self.BACK:
                row = row[half_point:]
            else:
                raise ValueError

        col = self.COLUMNS
        for pos in self._capture.group(2):
            half_point = (len(col) + 1) // 2
            if pos == self.LEFT:
                col = col[:half_point]
            elif pos == self.RIGHT:
                col = col[half_point:]
            else:
                raise ValueError

        _id = (row[0] * self.ID_SCALING) + col[0]

        return _id, row[0], col[0]

    @property
    def id(self) -> int:
        return self._id[0]

    @property
    def seat(self) -> tuple:
        return self._id[1], self._id[2]


def get_input(in_file):
    with open(in_file, 'r') as f:
        return [x.replace('\n', '') for x in f.readlines()]


def main():
    file_input = get_input(IN_FILE)

    ids = sorted([BoardingPassEntry(_entry).id for _entry in file_input])

    # part 1
    highest_id = ids[-1]
    print("Part 1:\n\tHighest ID:\t{}".format(highest_id))

    # part 2
    possible_id = [_id for _id in range(ids[0], ids[-1]) if _id not in ids][0]
    print("Part 2:\n\tLast ID:\t{}".format(possible_id))


if __name__ == '__main__':
    main()
