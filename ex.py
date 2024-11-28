x = 2
y = 0
while x < 140:
    while y < 400:
        z = 15 - x + y
        if z > 0 and z == 0.5 * x:
            if (1540 - 6 * y - x) % 4 == 0:
                t = (1540 - 6 * y - x) / 4
                w = 400 - x - y - z - t
                if w > 0:
                    print(f"{x} ,{y} ,{z} ,{t} ,{w}")
        y += 1
    x += 2
