import re

IN_FILE = 'day4-input.bat'
VALID_HEIGHT = r'(\d{3})cm|(\d{2})in'
VALID_HEX_COLOR = r'^(#[0-9A-Fa-f]{6})$'
VALID_EYE_COLOR = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
VALID_PASSPORT_ID = r'^([0-9]{9})$'


class PassportInfo(list):
    def __init__(self, pass_info):
        super().__init__()
        self._info = []
        if type(pass_info) == str:
            f = open(pass_info, 'r')
            in_list = [x.replace('\n', '') for x in f.readlines()]
            out_list = list()

            i = 0
            for line in in_list:
                if len(out_list) == i:
                    out_list.append({})
                line = line.replace('\n', '')
                if line != '':
                    line = line.split(' ')
                    for field in line:
                        info = field.split(':')
                        out_list[i][info[0]] = info[1]
                else:
                    i = i + 1
            self._info = out_list
        elif type(pass_info) == dict:
            self._info = pass_info
        else:
            raise TypeError

    def __getattr__(self, method):
        return getattr(self._info, method)

    def __getitem__(self, item):
        return self._info[item]

    def __iter__(self):
        return iter(self._info)

    def __len__(self):
        return len(self._info)

    def __str__(self):
        return str(self._info)

    @staticmethod
    def validate_field(field):
        valid_count = 0
        try:
            if 1920 <= int(field['byr']) <= 2002:
                valid_count = valid_count + 1
            if 2010 <= int(field['iyr']) <= 2020:
                valid_count = valid_count + 1
            if 2020 <= int(field['eyr']) <= 2030:
                valid_count = valid_count + 1
            if field['hgt']:
                height = re.search(VALID_HEIGHT, field['hgt'])
                if height.group(1) is None:
                    if 59 <= int(height.group(2)) <= 76:
                        valid_count = valid_count + 1
                else:
                    if 150 <= int(height.group(1)) <= 193:
                        valid_count = valid_count + 1
            if re.search(VALID_HEX_COLOR, field['hcl']):
                valid_count = valid_count + 1
            if re.search(VALID_EYE_COLOR, field['ecl']):
                valid_count = valid_count + 1
            if re.search(VALID_PASSPORT_ID, field['pid']):
                valid_count = valid_count + 1
        except KeyError:
            pass
        except AttributeError:
            pass

        return valid_count == 7


def get_count_part1(pass_info):
    part1_count = 0
    for info_chunk in pass_info:
        required_length = 8

        if 'cid' not in info_chunk.keys():
            required_length = required_length - 1

        if len(info_chunk) == required_length:
            part1_count = part1_count + 1

    return part1_count


def get_count_part2(pass_info):
    part2_count = 0
    for info_chunk in pass_info:
        if pass_info.validate_field(info_chunk):
            part2_count = part2_count + 1

    return part2_count


def main():
    pass_info = PassportInfo(IN_FILE)

    part1_count = get_count_part1(pass_info)
    part2_count = get_count_part2(pass_info)

    print("Valid Passport Identification Fields (Part 1):\t{}".format(part1_count))
    print("Valid Passport Identification Fields (Part 2):\t{}".format(part2_count))


if __name__ == '__main__':
    main()
