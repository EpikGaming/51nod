from functools import reduce
def lcs(a,b):
    lengha = len(a) + 1
    lenghb = len(b) + 1
    matrixflag = [[0 for i in range(lenghb)]for j in range(lengha)]
    matrixnum = [[0 for i in range(lenghb)]for j in range(lengha)]
    #创造一个m+1行，n+1列的二维数组，matrixflag用于存放符号，matrixnum用于存放数值用于比较
    for i in range(lengha - 1):
        for j in range(lenghb - 1):
            if a[i] == b[j]:
                matrixnum[i + 1][j + 1] = matrixnum[i][j] + 1
                matrixflag[i + 1][j + 1] = 'OK'
            else:
                if matrixnum[i][j + 1] >= matrixnum[i + 1][j]:
                    matrixnum[i + 1][j + 1] = matrixnum[i][j + 1]
                    matrixflag[i + 1][j + 1] = 'UP'
                if matrixnum[i + 1][j] > matrixnum[i][j + 1]:
                    matrixnum[i + 1][j +1] =matrixnum[i + 1][j]
                    matrixflag[i + 1][j + 1] = 'LEFT'
    print(matrixnum)
    print(matrixflag)
    strA = ''
    x = len(a)
    y = len(b)
    c = matrixnum[x][y]
    while c != 0:
        if matrixflag[x][y] == 'UP':
            x -= 1
            c = matrixnum[x][y]
        elif matrixflag[x][y] == 'LEFT':
            y -= 1
            c = matrixnum[x][y]
        elif matrixflag[x][y] == 'OK':
            x -= 1
            y -= 1
            strA += a[x]
            c = matrixnum[x][y]
    print("strA = " + strA)
    strB = list(strA)
    strB = "".join(strB[::-1])
    print("strB = " + strB)
    strC = reduce(lambda x,y:y+x,strA)
    print("strC = " + strC)
a = input()
b = input()
lcs(a,b)

'''
给出两个字符串A B，求A与B的最长公共子序列（子序列不要求是连续的）。
比如两个串为：
abcicba
abdkscab
ab是两个串的子序列，abc也是，abca也是，其中abca是这两个字符串最长的子序列。

动态规划题，需要构造一个m+1 * n+1的二维数组，自底向上进行递归
其中，用于存放数值的二维数组的递归式为：
         {0                             if i ==0 or j == 0
c[i,j] = {c[i - 1,j - 1] + 1            if i,j > 0 and Xi == Yj
         {max(c[i,j - 1],c[i - 1,j])    if i,j > 0 and Xi != Yj
Input：
abcicba
abdkscab
Output：
abca
'''