import numpy as np


def estimate_pi(n):
    x_squared = np.power(np.random.uniform(-1, 1, n), 2)
    y_squared = np.power(np.random.uniform(-1, 1, n), 2)
    r_squared = np.add(x_squared, y_squared)
    prob_circle = np.count_nonzero(r_squared <= 1) / n
    pi = 4 * prob_circle
    return pi


if __name__ == '__main__':
    pi = estimate_pi(1000000)
    assert pi < 3.15 and pi > 3.13