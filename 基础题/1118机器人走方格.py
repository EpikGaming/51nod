#组合数学方法
import math
M,N = map(int,input().split(" "))
ans = math.factorial(M + N - 2) // math.factorial(M - 1) // math.factorial(N - 1) % (10 ** 9 + 7)
print(ans)

#迭代法
M,N = map(int,input().split(" "))
matrix =[[0 for j in range(M)] for i in range(N)]
matrix[0] = [1] * M
for i in range(N):
    matrix[i][0] = 1
for i in range(1,N):
    for j in range(1,M):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
ans = int(matrix[-1][-1])
print(ans % (10 ** 9 + 7))