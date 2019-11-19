def longest_common_prefix(string_list):
    string_list.sort()
    temp = ''
    prefix = []
    for s in string_list[0]:
        temp += s
        count = 0
        for string in string_list:
            if temp in string:
                count += 1
                if count == len(string_list):
                    prefix = temp
    return prefix


print(longest_common_prefix(["abcdefgh", "aefghijk", "abcefgh"]))
print(longest_common_prefix(["abcab", "abc", "abcd"]))
