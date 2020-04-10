
def max_array(array, k):
    result = []
    for i in range(len(array)):
        if i + k > len(array):
            break
        else:
            sub_array = array[i: min(len(array) + 1, i + k)]
            sub_array_max = max(sub_array)
            result.append(sub_array_max)
    return result


if __name__ == '__main__':
    assert max_array([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
    assert max_array([10, 5, 2, 7, 8, 7], 4) == [10, 8, 8]
    assert max_array([10, 5, 2, 7, 8, 7], 6) == [10]