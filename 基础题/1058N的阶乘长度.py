import math
n = int(input())
x = n * math.log10(n / math.e) + 0.5 * math.log10(2 * math.pi * n)
print(int(x + 1))
'''
输入N求N的阶乘的10进制表示的长度。例如6! = 720，长度为3。

数论题，运用斯特林公式求N的阶乘的位数，看笔记
Input：
6
Output：
3
'''