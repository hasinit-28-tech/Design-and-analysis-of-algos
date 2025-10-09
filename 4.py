#4. Matrix Creation and Value Fetch
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * n + j + 1)  
        matrix.append(row)
    return matrix


n = 3
matrix = create_matrix(n)
print(f"{n}x{n} Matrix:")
for row in matrix:
    print(row)


try:
    i = int(input(f"Enter row (0-{n-1}): "))
    j = int(input(f"Enter column (0-{n-1}): "))
    print(f"Value at ({i}, {j}): {matrix[i][j]}")
except:
    print("Invalid input!")