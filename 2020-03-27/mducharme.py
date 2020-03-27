"""
author: mikaeld
"""

from typing import List


def lowest_positive_integer(array: List[int]) -> int:
    positive_only = {i for i in array if i >= 0}

    if not positive_only:
        return 0

    max_val = max(positive_only)
    min_val = min(positive_only)

    linear_array = {i for i in range(min_val, max_val + 1)}

    difference = linear_array.difference(positive_only)
    if difference:
        return min(difference)

    return max_val + 1


if __name__ == '__main__':
    in_1 = [3, 4, -1, 1]
    in_2 = [1, 2, 0]
    in_3 = [1, 1, -1, 3, 5, 6, 7, 10, 3]
    in_4 = [-1, -2, -3]
    in_5 = [-1, -2, -3, 0]

    assert lowest_positive_integer(in_1) == 2
    assert lowest_positive_integer(in_2) == 3
    assert lowest_positive_integer(in_3) == 2
    assert lowest_positive_integer(in_4) == 0
    assert lowest_positive_integer(in_5) == 1
