def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle


triangle = generate_pascals_triangle(5)
print(triangle[2][1])


def print_update_down_pascals_triangle1(h):
    triangle = generate_pascals_triangle(h)

    for i in range(h - 1, -1, -1):
        print(" " * (h - i - 1), end="")
        for num in triangle[i]:
            print(num, end=" ")
        print()


# print_update_down_pascals_triangle1(6)
# list1 = [1,2,3,4]
# for i in range(len(list1)):
#     print(list1[i])
# for i in list1:
#     print(i)
#     if i == 3:
#         break
# print(list1)
