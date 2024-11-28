# a + b + c + d + e = 400
# 10a + 8b + 12c + 9d + 11e = 3630
# 2d =  a
# b = a + c - 15


# 3d + b + c + = 400 - e
# 29d + 8b + 12c = 3630 - 11e
# 2d - b + c = 15
d = 0
list_result = []
for e in range(378):
    d = 83 - 0.2 * e
    a = 2 * d
    b = 151 - 0.4 * e
    c = 0
    res = []
    res.append(round(a, 2))
    res.append(round(b, 2))
    res.append(round(c, 2))
    res.append(round(d, 2))
    res.append(round(e, 2))

    if a >= 0 and b >= 0:
        list_result.append(list_result)
for i in range(len(list_result)):
    for j in range(len(list_result[i])):
        print(f"{list_result[i][j]} ", end=" ")
    print()
