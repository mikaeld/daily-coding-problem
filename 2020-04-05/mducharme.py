"""
author: mikaeld
"""


def longest_substring(input_string: str, k: int):
    result_substring = ''

    for index in range(len(input_string)):

        for reader_position in range(index, len(input_string)):
            substring = input_string[index:reader_position+1]
            unique_characters = set(substring)

            if len(unique_characters) <= k:
                if len(substring) > len(result_substring):
                    result_substring = substring

            else:
                break

    return result_substring


if __name__ == '__main__':
    assert longest_substring('abcba', 2) == 'bcb'
    assert longest_substring('aasdqwwwss', 2) == 'wwwss'
