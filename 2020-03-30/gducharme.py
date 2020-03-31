
# def count(s):
#     if len(s) == 0 or len(s) == 1:
#         result = 1
#     else:
#         result = count(s[:-1]) + (count(s[:-2]) if int(s[-2:]) <= 26 else 0)
#     return result

def count(s):
    result = 1 if len(s) == 0 or len(s) == 1 else count(s[:-1]) + (count(s[:-2]) if int(s[-2:]) <= 26 else 0)
    return result


if __name__ == '__main__':
    assert count('111') == 3
    assert count('1112') == 5
    assert count('3326') == 2
    assert count('911') == 2
