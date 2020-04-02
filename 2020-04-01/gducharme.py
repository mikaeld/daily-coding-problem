# My solution: does not work for all cases


def sum_adjacent(input):
    length = len(input)
    indexes = list(range(1, length + 1))
    input = [0] + input + [0]

    while indexes:
        #Calculate gain and find max gain
        input_gain  = [input[i] - input[i - 1] - input[i + 1] for i in indexes]
        index_input_gain = input_gain.index(max(input_gain))  # problem if there are multiple max gains
        index = indexes[index_input_gain]
        # Delete unavailable indexes
        indexes.remove(index)
        if index - 1 in indexes:
            indexes.remove(index - 1)
        if index + 1 in indexes:
            indexes.remove(index + 1)
        # Change unavailable input values to 0
        input[index - 1], input[index + 1] = 0, 0     

    result = sum(input)

    return result


# Not my solution: works for all cases


def sum_adjacent(input):
    sum_excluding = 0
    sum_including = 0
    sum_max = max(sum_excluding, sum_including)
    
    for value in input:
        sum_excluding, sum_including = sum_max, sum_excluding + value
        sum_max = max(sum_excluding, sum_including)
    return sum_max

if __name__ == '__main__':
    assert sum_adjacent([2, 4, 6, 2, 5]) == 13
    assert sum_adjacent([5, 1, 1, 5]) == 10
    assert sum_adjacent([5, 2, 7, 7, 20, 10, 1, 4, 9]) == 42
    assert sum_adjacent([-5, 0, -2, 22, 24, -20, 7, 2, 0]) == 31
    assert sum_adjacent([1, 2, 10, 20, 11]) == 21   # should give 22


