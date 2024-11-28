h = 6
k = 0
for g in range(4, h + 1):
    k += 1
    print(k)
for i in range(2 * h - 1):
    for j in range(2 * h - 1):
        if h % 2 == 1:
            if (
                2 * h + k >= i + j >= h - 1
                and j <= i + h - 1
                and i <= j + h - 1
                and (i + j) % 2 == 0
            ):
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        else:
            if (
                2 * h + k >= i + j >= h - 1
                and j <= i + h - 1
                and i <= j + h - 1
                and (i + j) % 2 == 1
            ):
                print("* ", end=" ")
            else:
                print("  ", end=" ")
    print()
