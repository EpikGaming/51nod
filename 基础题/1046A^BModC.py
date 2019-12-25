listA = input().split()
a = int(listA[0])
b = int(listA[1])
c = int(listA[2])
print(pow(a,b,c))
x = 1
while b != 0:
    if (b & 1) == 1:
        x = (x * a) % c
    b >>= 1
    a = (a * a) % c
print(x)
'''
给出3个正整数A B C，求A^B Mod C。
例如，3 5 8，3^5 Mod 8 = 3。

数论题，快速幂思想，但是python中的pow()函数自带求解x ^ y Mod z的方法
直接调用函数即可
Input：
3 5 8
Output：
3
'''