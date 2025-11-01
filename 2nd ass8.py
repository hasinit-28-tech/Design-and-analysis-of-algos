def matrix_multiply(A, B):
   
    m = len(A)
    p = len(A[0]) if A else 0
    assert p == len(B), "Incompatible dimensions"
    n = len(B[0])
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s = 0
            for k in range(p):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

# Example:
A = [[1,2,3],[4,5,6]]  
B = [[7,8],[9,10],[11,12]]  
print("Product:", matrix_multiply(A,B))
