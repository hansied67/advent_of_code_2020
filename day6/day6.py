IN_FILE = 'day6-input.txt'


def get_input(in_file: str) -> list:
    survey_results = []
    with open(in_file, 'r') as f:
        survey_results = [x.replace('\n', '') for x in f.readlines()]

    results_fixed = list(list())
    results_fixed.append(list())
    i = 0
    for x in survey_results:
        if x != '':
            results_fixed[i].append(x)
        else:
            results_fixed.append(list())
            i = i + 1

    return results_fixed


def count_unique_answers(survey_result: list) -> int:
    unique_chars = list()
    [unique_chars.append(x) for x in ''.join(survey_result) if x not in unique_chars]
    return len(unique_chars)


def count_unanimous_answers(survey_result: list) -> int:
    unanimous_answers_temp = survey_result[0]
    unanimous_answers = survey_result[0]

    if len(survey_result) != 1:
        for answer_block in survey_result[1:]:
            for answer in unanimous_answers_temp:
                if answer not in answer_block and unanimous_answers:
                    unanimous_answers = unanimous_answers.replace(answer, '')

    return len(unanimous_answers)


def main():
    survey_results = get_input(IN_FILE)

    # Part 1
    unique_answers = 0
    for result in survey_results:
        unique_answers = unique_answers + count_unique_answers(result)
    print(unique_answers)

    # Part 2
    unanimous_answers = 0
    for result in survey_results:
        unanimous_answers = unanimous_answers + count_unanimous_answers(result)
    print(unanimous_answers)


if __name__ == '__main__':
    main()