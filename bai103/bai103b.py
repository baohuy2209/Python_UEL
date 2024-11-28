n = 6


def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j] + 1)
        row.append(1)
        triangle.append(row)
    return triangle


list_index = [0] * n
triangle = generate_pascals_triangle(n)
for i in range(2 * n - 1):
    for j in range(n):
        if n % 2 == 1:
            if i <= j + n - 1 and i + j >= n - 1 and (i + j) % 2 == 0:
                print(f"{triangle[j][list_index[j]]} ", end="  ")
                if list_index[j] <= len(triangle[j]):
                    list_index[j] += 1
            elif i + j % 2 == 1:
                print("  ", end="  ")
            else:
                print("  ", end="  ")
        else:
            if i <= j + n - 1 and i + j >= n - 1 and (i + j) % 2 == 1:
                print(f"{triangle[j][list_index[j]]} ", end="  ")
                if list_index[j] <= len(triangle[j]):
                    list_index[j] += 1
            elif i + j % 2 == 0:
                print("  ", end="  ")
            else:
                print("  ", end="  ")
    print()
