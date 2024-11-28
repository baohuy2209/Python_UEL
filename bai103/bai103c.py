n = 5


def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j] + 1)
        row.append(1)
        triangle.append(row)
    return triangle


list_index = [0] * n  # list_index[1] = 0
print(list_index)
triangle = generate_pascals_triangle(n)[::-1]
for i in range(2 * n - 1):
    for j in range(n):
        if 2 * j <= i + j <= 2 * n - 2 and (i + j) % 2 == 0:
            print(f"{triangle[j][list_index[j]]} ", end="  ")
            if list_index[j] <= len(triangle[j]):
                list_index[j] += 1
        elif i + j % 2 == 1:
            print("  ", end="  ")
        else:
            print("  ", end="  ")
    print()
