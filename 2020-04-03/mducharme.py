"""
author: mikaeld
"""


def auto_complete(query: str, array: list):
    return [match for match in array if query in match]


if __name__ == '__main__':
    array = ['dog', 'deer', 'deal']
    print(auto_complete('de', array))
