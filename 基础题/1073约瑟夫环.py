listA = input().split()
n = int(listA[0])
k = int(listA[1])
result = 0
for i in range(2,n + 1):
    result = (result + k) % i
print(result + 1)
'''
N个人坐成一个圆环（编号为1 - N），从第1个人开始报数，数到K的人出列，
后面的人重新从1开始报数。问最后剩下的人的编号。
例如：N = 3，K = 2。2号先出列，然后是1号，最后剩下的是3号。

约瑟夫环问题，用到了递归，记笔记上了
Input：
3 2
Output：
3
'''

def josepg(n,m):
    if(n == 1):
        return n
