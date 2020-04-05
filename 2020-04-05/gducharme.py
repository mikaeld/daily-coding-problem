

def longest_substring(k, string):
    if k == 0 or string == "":
        return 0
    final_string = ""
    for i, s in enumerate(string):
        substring = s
        j = 1
        add_character = i + j < len(string)
        while add_character:
            substring_try = string[i:i + j + 1]
            if len(set(substring_try)) <= k:
                substring = substring_try
                j += 1
                add_character = i + j < len(string)
            else:
                add_character = False
        final_string = substring if len(substring) > len(final_string) else final_string
    return len(final_string)


if __name__ == '__main__':
    assert longest_substring(2, "abcba") == 3
    assert longest_substring(3, "patate") == 5        
    assert longest_substring(1, "patate") == 1 
    assert longest_substring(0, "patate") == 0 
    assert longest_substring(3, "") == 0 