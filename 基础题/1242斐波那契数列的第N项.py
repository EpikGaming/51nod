def mult(matrixA,matrixB):
    matrixC = [[sum(a * b for a, b in zip(m1, m2)) % 1000000009 for m2 in zip(*matrixA)] for m1 in matrixB]
    return matrixC

def Fib(N):
    if N == 1:
        return 1
    A = [[1,1],[1,0]]
    res = [[1,0],[0,1]]
    while N:
        if N & 1:
            res = mult(res,A)
        A = mult(A,A)
        N >>= 1
    return res[0][1]

N = int(input())
print(Fib(N))