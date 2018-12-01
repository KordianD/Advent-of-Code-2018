def part_one(data_input: list) -> int:
    frequency = 0
    for line in data_input:
        frequency += int(line)
    return frequency


def part_two(data_input: list) -> int:
    summed_freq = {0: 1}
    not_found = True

    cumulative_frequency = 0

    while not_found:
        for elem in data_input:
            cumulative_frequency += elem
            if cumulative_frequency in summed_freq:
                return cumulative_frequency

            summed_freq[cumulative_frequency] = 1

    raise ValueError("There is no repetition of frequency")
