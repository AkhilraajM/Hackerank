def pascals_triangle(n):
    pascals_list = [[1]]
    for i in range(n):
        for j in range(len(pascals_list[i])):
            if j == 0:
                pascals_list.append([1])
            if j == len(pascals_list[i]) - 1:
                pascals_list[i + 1].append(1)
            else:
                pascals_list[i + 1].append(pascals_list[i][j] + pascals_list[i][j + 1])
    return pascals_list


print(pascals_triangle(10))
