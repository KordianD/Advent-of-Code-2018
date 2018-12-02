def part_one(data_input: list) -> int:
    how_many_twos: int = 0
    how_many_threes: int = 0
    for line in data_input:
        founded_twos, founded_tree = calculate_how_many_twos_and_threes(line)
        how_many_twos += founded_twos
        how_many_threes += founded_tree

    return how_many_threes * how_many_twos


def part_two(data_input: list) -> str:
    data_input.sort()

    for i in range(len(data_input) - 1):
        difference: int = 0
        index: int = 0
        letter_index: int = 0

        for first, second in zip(data_input[i], data_input[i + 1]):
            if first != second:
                difference += 1
                letter_index = index

            index += 1
        if difference == 1:
            return data_input[i][:letter_index] + data_input[i][letter_index + 1:]

    return None


def calculate_how_many_twos_and_threes(line: list) -> tuple:
    dictionary: dict = {}
    for elem in line:
        if elem not in dictionary:
            dictionary[elem] = 1
        else:
            dictionary[elem] += 1

    return int(2 in dictionary.values()), int(3 in dictionary.values())
