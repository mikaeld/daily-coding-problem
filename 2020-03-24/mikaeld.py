"""
author: mikaeld
"""


def solution(input, k):
    # convert input to immutable type
    input = tuple(input)
    results = list()
    for index, value in enumerate(input):
        # convert to mutable type
        input_copy = list(input)
        input_copy.pop(index)
        results.append(k - value in input_copy)
    return True in results


if __name__ == '__main__':
    assert solution(input=[10, 15, 3, 7], k=17) == True
    assert solution(input=[10, 15, 3, 7], k=20) == False
    assert solution(input=[10, 15, 3, 7, 10], k=20) == True

