import re

IN_FILE = 'day7-input.txt'

BAG_TYPE = 'shiny gold'
COLOR_REGEX = r'(.+?) bags'
CONTAINS_REGEX = r'(\d+) (.+?) bag'


def get_input(in_file: str) -> dict:
    graph = {}
    with open(in_file, 'r') as f:
        for line in f.readlines():
            color = re.match(COLOR_REGEX, line).group(1)
            contains = re.findall(CONTAINS_REGEX, line)
            graph[color] = contains
    return graph


def has_bag_type(bag_type: str, color: str, graph: dict) -> bool:
    if color == bag_type:
        return True
    return any(has_bag_type(bag_type, c, graph) for _, c in graph[color])


def count(bag_type: str, graph: dict) -> int:
    return 1 + sum(int(n)*count(c, graph) for n, c in graph[bag_type])


def main():
    graph = get_input(IN_FILE)

    part1 = sum(has_bag_type(BAG_TYPE, c, graph) for c in graph.keys()) - 1
    part2 = count(BAG_TYPE, graph) - 1

    print("Part 1:\n\tBags that can hold shiny gold bags:\n\t\t{}".format(part1))
    print("Part 2:\n\tRequired amount of bags in 1 shiny gold bag:\n\t\t{}".format(part2))


if __name__ == '__main__':
    main()
