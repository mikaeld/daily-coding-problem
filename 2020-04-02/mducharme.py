"""
author: mikaeld
"""
import threading


def test_function():
    print(f'Non blocking call of test_function')
    return f'test value'


def scheduler(f, n):
    delay_s = n * 1e-3
    timer = threading.Timer(delay_s, f)
    timer.start()


if __name__ == '__main__':
    print('This is printed before scheduling the job')
    scheduler(test_function, 5000)
    print('This is printed after scheduling the job, but before the function call')