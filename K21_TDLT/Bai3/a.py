import math


def calculate(n):
    s = math.sqrt(n)
    for i in range(n - 1, 0, -1):
        s = math.sqrt(i + s)
    return s


print(calculate(3))
