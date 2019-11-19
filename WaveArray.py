def wave_array(given_list):
    given_list = sorted(given_list)
    for i in range(0, len(given_list) - 1, 2):
        given_list[i], given_list[i + 1] = given_list[i + 1], given_list[i]
    return given_list


print(wave_array([2, 6, 1]))
print(wave_array([1, 2, 3, 4, 5, 6]))
