def Judge(a,b,c,d):
    ab = [b[0] - a[0],b[1] - a[1],b[2] - a[2]]
    ac = [c[0] - a[0],c[1] - a[1],c[2] - a[2]]
    cd = [d[0] - c[0],d[1] - c[1],d[2] - c[2]]
    ans = ab[0] * ac[1] * cd[2] + ac[0] * cd[1] * ab[2] + cd[0] * ab[1] * ac[2]
    ans -= ab[0] * cd[1] * ac[2] + ac[0] * ab[1] * cd[2] + cd[0] * ac[1] * ab[2]
    if ans == 0:
        print("Yes")
    else:
        print("No")

T = int(input())
for i in range(T):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    Judge(a,b,c,d)
