def part_one(data_input: list) -> int:
    frequency = 0
    for line in data_input:
        frequency += int(line)
    return frequency


def part_two(data_input: list) -> int:
    change_after_iteration = sum(data_input)
    if not change_after_iteration:
        return change_after_iteration

    best_n_repetition = float("inf")
    frequency = 0

    first_row = []
    for elem in data_input:
        first_row.append(frequency + elem)
        frequency += elem

    for elem in first_row:
        for rep in first_row:
            if (rep - elem) % change_after_iteration == 0 and best_n_repetition > (
                    rep - elem) / change_after_iteration and rep - elem > 0:
                best_n_repetition = (rep - elem) / change_after_iteration
                frequency = rep

    return frequency
