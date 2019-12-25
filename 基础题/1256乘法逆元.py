'''M,N = map(int,input().split())
for K in range(N):
    if (K * M % N) == 1:
        print(K)
        break
'''
def euler(P):
    ans = P
    for i in range(2,int(P ** 0.5 + 1)):
        if P % i == 0:
            ans -= ans / i
            while P % i == 0:
                P /= i
    if P > 1:
        ans -= ans / P
    return int(ans)

def Fermat(M,N,ans):
    result = pow(M,ans - 1,N)
    return result

M,N = map(int,input().split())
ans = euler(N)
K = Fermat(M,N,ans)
print(K)