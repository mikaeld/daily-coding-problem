"""
author: mikaeld
"""


def find_possible_decodings(input_sequence: str, mapping: dict) -> int:
    # Keep values that exist in the input sequence
    existing_values = [value for value in mapping.values() if value in input_sequence]
    combinations_found = 0

    def recursive_search(remaining_string):
        nonlocal combinations_found
        nonlocal existing_values

        for caracter in existing_values:
            if remaining_string.find(caracter) == 0:

                new_altered_string = remaining_string[len(caracter):]
                if len(new_altered_string) == 0:
                    combinations_found += 1
                else:
                    recursive_search(new_altered_string)

    recursive_search(input_sequence)

    return combinations_found


if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mapping = {letter: str(index + 1) for index, letter in enumerate(letters)}

    assert find_possible_decodings('1112', mapping) == 5
    assert find_possible_decodings('111', mapping) == 3
    assert find_possible_decodings('3326', mapping) == 2

