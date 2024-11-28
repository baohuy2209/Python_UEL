n = 7
for i in range(n):
    for j in range(2 * n - 1):
        if (
            i + j == n // 2
            or i == j + n // 2
            or j == i + n // 2
            or j == i + n + 1
            or i + j == 2 * n
            or i + j == n + 1
        ):
            if i <= n // 2:
                print(f"{i+1} ", end=" ")
            else:
                print(f"{n-i} ", end=" ")
        else:
            print("  ", end=" ")
    print()
