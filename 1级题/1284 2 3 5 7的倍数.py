N = int(input())
res = N
res -= (N // 2 + N // 3 + N // 5 + N // 7)
res += (N // 6 + N // 10 + N // 14 + N // 15 + N // 21 + N // 35)
res -= (N // 30 + N // 42 + N // 70 + N // 105)
res += (N // 210)
print(res)