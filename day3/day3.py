IN_FILE = 'day3-input.txt'


def get_input(in_file):
    f = open(in_file, 'r')
    in_list = f.readlines()
    f.close()
    return [x.replace('\n', '') for x in in_list]


class TobogganMap(object):

    snow = '.'
    tree = '#'

    def __init__(self, in_file):
        list_repr = get_input(in_file)
        self.initial_map = list_repr
        self.toboggan_map = list_repr
        self.size = (len(self.toboggan_map), len(self.toboggan_map[0]))  # (y, x)

    def expand_map(self):
        self.toboggan_map = [self.toboggan_map[i]+self.initial_map[i] for i in range(len(self.toboggan_map))]

    def verify_movement(self, new_coord):
        return self.toboggan_map[new_coord[0]][new_coord[1]] == self.snow

    def get_list_repr(self):
        return self.toboggan_map


class Sledder(object):

    def __init__(self, toboggan_map):
        self.toboggan_map = toboggan_map
        self.tree_hits = 0
        self.pos = (0, 0)

    # (y, x)
    def move(self, movement):
        self.pos = tuple(sum(x) for x in zip(self.pos, movement))
        if self.pos[0] >= (len(self.toboggan_map.get_list_repr())):
            return False
        elif self.pos[1] >= len(self.toboggan_map.get_list_repr()[0]):
            self.toboggan_map.expand_map()
        if not self.toboggan_map.verify_movement(self.pos):
            self.tree_hits = self.tree_hits + 1
        return True

    def get_tree_hits(self):
        return self.tree_hits

    def start_over(self):
        self.pos = (0, 0)
        self.tree_hits = 0


def main():
    toboggan_map = TobogganMap(IN_FILE)
    sledder_part1 = Sledder(toboggan_map)
    while sledder_part1.move((1, 3)):
        pass
    print(sledder_part1.get_tree_hits())

    sledder_part2 = Sledder(toboggan_map)
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    slope_hits = []
    for slope in slopes:
        while sledder_part2.move(slope):
            pass
        slope_hits.append(sledder_part2.get_tree_hits())
        sledder_part2.start_over()

    print(slope_hits)
    hits_product = 1
    for hit in slope_hits:
        hits_product = hits_product * hit

    print(hits_product)


if __name__ == '__main__':
    main()
