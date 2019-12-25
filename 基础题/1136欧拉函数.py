N = int(input())
ans = N
for i in range(2,int(N ** 0.5 + 1)):
    if N % i == 0:
        ans -= ans / i
        while N % i == 0:
            N /= i
if N > 1:
    ans -= ans / N
print(int(ans))