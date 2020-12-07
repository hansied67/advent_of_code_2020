import sys
import re

IN_FILE = 'day7-input.txt'


def get_input(in_file: str) -> dict:
    graph = {}
    with open(in_file, 'r') as f:
        for line in f.readlines():
            color = re.match(r'(.+?) bags', line).group(1)
            contains = re.findall(r'(\d+) (.+?) bag', line)
            graph[color] = contains
    return graph


def has_shiny(color, graph):
    if color == 'shiny gold':
        return True
    return any(has_shiny(c, graph) for _, c in graph[color])


def count(bag_type, graph):
    return 1 + sum(int(n)*count(c, graph) for n, c in graph[bag_type])


def main():
    graph = get_input(IN_FILE)
    
    print(sum(has_shiny(c, graph) for c in graph.keys()) - 1)
    print(count('shiny gold', graph) - 1)


if __name__ == '__main__':
    main()
