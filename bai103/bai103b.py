def generate_pascals_triangle(n): 
    triangle = [[1]]
    for i in range(1, n): 
        row=[1]
        for j in range(1, i): 
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
def print_triangle(h):
    triangle = generate_pascals_triangle(h)
    print(triangle)
print_triangle(5)