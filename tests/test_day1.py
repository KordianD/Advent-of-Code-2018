from solutions.day1 import part_one, part_two


def test_should_return_correct_value_for_read_input():
    read_input = [int(line) for line in open('input/Day1.txt')]
    assert part_one(read_input) == 531


def test_should_return_correct_value_for_given_test_examples():
    first_example = [1, -1]
    second_example = [3, 3, 4, -2, -4]
    third_example = [-6, 3, 8, 5, -6]
    fourth_example = [7, 7, -2, -7, -4]

    assert part_two(first_example) == 0
    assert part_two(second_example) == 10
    assert part_two(third_example) == 5
    assert part_two(fourth_example) == 14


def test_should_return_correct_value_when_complex_example():
    complexity_example = [2349656348557312, -1174828174278656, -1174828174280793]

    assert part_two(complexity_example) == 2349656348557312
