import re
from copy import deepcopy

IN_FILE = 'day8-input.txt'

INSTRUCTION_REGEX = r'(\w+) [+]*(-*\d+)'
ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def get_input(in_file: str) -> list:
    _input = list()
    with open(in_file, 'r') as f:
        _input = [x.replace('\n', '') for x in f.readlines()]
    return _input


def nop(instructions_dict: dict, cur_line: int):
    instructions_dict[cur_line][1] = instructions_dict[cur_line][1] + 1
    return instructions_dict, cur_line+1


def acc(instructions_dict: dict, count: int, cur_line: int, param: int):
    instructions_dict[cur_line][1] = instructions_dict[cur_line][1] + 1
    return instructions_dict, count+param, cur_line+1


def jmp(instructions_dict: dict, cur_line: int, param: int):
    instructions_dict[cur_line][1] = instructions_dict[cur_line][1] + 1
    return instructions_dict, cur_line+param


def do_instruction_until_repeat(instructions_dict: dict, instruction: str, count=0, cur_line=0) -> int:
    _regex_match = re.match(INSTRUCTION_REGEX, instruction)
    _op_code = _regex_match.group(1)
    _param = int(_regex_match.group(2))

    if _op_code == NOP:
        instructions_dict, cur_line = nop(instructions_dict, cur_line)
    elif _op_code == ACC:
        instructions_dict, count, cur_line = acc(instructions_dict, count, cur_line, _param)
    elif _op_code == JMP:
        instructions_dict, cur_line = jmp(instructions_dict, cur_line, _param)
    else:
        return 0

    if cur_line < len(instructions_dict) and instructions_dict[cur_line][1] < 1:
        count = do_instruction_until_repeat(instructions_dict, instructions_dict[cur_line][0], count, cur_line)
    return count


def do_instruction_until_repeat_if_reaches_eof(instructions_dict: dict,
                                               instruction: str, count=0, cur_line=0, eof=False) -> tuple:
    _regex_match = re.match(INSTRUCTION_REGEX, instruction)
    _op_code = _regex_match.group(1)
    _param = int(_regex_match.group(2))

    if _op_code == NOP:
        instructions_dict, cur_line = nop(instructions_dict, cur_line)
    elif _op_code == ACC:
        instructions_dict, count, cur_line = acc(instructions_dict, count, cur_line, _param)
    elif _op_code == JMP:
        instructions_dict, cur_line = jmp(instructions_dict, cur_line, _param)
    else:
        return 0, False

    if cur_line < len(instructions_dict) and instructions_dict[cur_line][1] < 1:
        count, eof = do_instruction_until_repeat_if_reaches_eof(instructions_dict, instructions_dict[cur_line][0],
                                                                count, cur_line, eof)
    else:
        if len(instructions_dict) == cur_line:
            eof = True
            return count, eof
    if not eof:
        count = 0
    return count, eof


def main():
    instructions_dict = {c: [x, 0] for c, x in enumerate(get_input(IN_FILE))}

    part1 = deepcopy(instructions_dict)
    part2 = deepcopy(instructions_dict)

    count = do_instruction_until_repeat(part1, part1[0][0])
    print(count)

    for _c, _instruction in part2.items():
        instructions_dict_temp = deepcopy(part2)
        instruction_pre_mod = _instruction[0].split(' ')[0]
        if instruction_pre_mod == NOP:
            instruction_pre_mod = JMP
        elif instruction_pre_mod == JMP:
            instruction_pre_mod = NOP
        else:
            continue

        instructions_dict_temp[_c] = [' '.join([instruction_pre_mod, _instruction[0].split(' ')[1]]), 0]

        count_fixed = do_instruction_until_repeat_if_reaches_eof(instructions_dict_temp, instructions_dict_temp[0][0])

        if count_fixed[1]:
            print(count_fixed[0])


if __name__ == '__main__':
    main()
