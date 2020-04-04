

def steps_one_two(n):
    if n == 0 or n == 1:
        ways = 1
    else:
        ways = steps_one_two(n-1) + steps_one_two(n-2)
    return ways


if __name__ == '__main__':
    assert steps_one_two(4) == 5


def steps_x(n, X):
    ways = 0
    if n == 0:
        ways = 1
    else:
        for x in X:
            if x <= n:
                ways += steps_x(n-x, X)
    return ways


if __name__ == '__main__':
    assert steps_x(4, [1, 2]) == 5
    assert steps_x(5, [1, 3, 5]) == 5
    assert steps_x(1, [2]) == 0
    assert steps_x(1, [1, 2, 3]) == 1
    assert steps_x(6, [1, 2, 3, 4]) == 29