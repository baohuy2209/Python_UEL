n = 5


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def nCk(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


list_index = [0] * n
for i in range(2 * n - 1):
    for j in range(n):
        if n % 2 == 1:
            if i <= j + n - 1 and i + j >= n - 1 and (i + j) % 2 == 0:
                print(f"{int(nCk(j,list_index[j]))} ", end="  ")
                list_index[j] += 1
            elif i + j % 2 == 1:
                print("  ", end="  ")
            else:
                print("  ", end="  ")
        else:
            if i <= j + n - 1 and i + j >= n - 1 and (i + j) % 2 == 1:
                print(f"{int(nCk(j,list_index[j]))} ", end="  ")
                list_index[j] += 1
            elif i + j % 2 == 0:
                print("  ", end="  ")
            else:
                print("  ", end="  ")
    print()
