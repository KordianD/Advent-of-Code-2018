from solutions.day2 import part_one, part_two


def test_should_return_correct_value_for_read_input():
    read_input = [line.strip() for line in open('input/Day2.txt')]
    assert part_one(read_input) == 5704


def test_should_return_correct_value_for_given_test_examples():
    test_array: list = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

    assert part_one(test_array) == 12


def test_should_return_correct_string_of_difference_for_test_examples():
    test_array: list = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

    assert part_two(test_array) == 'fgij'


def test_should_return_correct_string_for_read_input():
    read_input = [line.strip() for line in open('input/Day2.txt')]
    assert part_two(read_input) == 'umdryabviapkozistwcnihjqx'
