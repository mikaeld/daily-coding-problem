"""
author: mikaeld
"""


def multiply(input):
    # find element-wise multiplication total
    array = iter(input)
    total = next(array)

    for element in array:
        total *= element

    # return list of total / each element of the input array
    return list(map(lambda x: int(total / x), input))


def multiply_follow_up(input):

    result = list()
    for index in range(len(input)):

        partial_array = input[:index]
        if index < len(input):
            partial_array += input[index+1:]

        array = iter(partial_array)
        total = next(array)

        for element in array:
            total *= element

        result.append(total)

    return result


if __name__ == '__main__':
    input_1 = [1, 2, 3, 4, 5]
    input_2 = [3, 2, 1]

    assert multiply(input_1) == [120, 60, 40, 30, 24]
    assert multiply(input_2) == [2, 3, 6]

    assert multiply_follow_up(input_1) == [120, 60, 40, 30, 24]
    assert multiply_follow_up(input_2) == [2, 3, 6]




