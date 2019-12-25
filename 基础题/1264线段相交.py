def Judge(a,b,c,d):
    ab = [b[0] - a[0],b[1] - a[1]]
    ac = [c[0] - a[0],c[1] - a[1]]
    ad = [d[0] - a[0],d[1] - a[1]]
    ca = [a[0] - c[0],a[1] - c[1]]
    cb = [b[0] - c[0],b[1] - c[1]]
    cd = [d[0] - c[0],d[1] - c[1]]
    if (((ac[0] * ab[1]) - (ac[1] * ab[0])) * ((ad[0] * ab[1]) - (ad[1] * ab[0])) <= 0) and (((ca[0] * cd[1]) - (ca[1] * cd[0])) * ((cb[0] * cd[1]) - (cb[1] * cd[0])) <= 0):
        return True
    return False
T = int(input())
listB = []
for i in range(T):
    listA = list(map(int, input().split()))
    a = [listA[0], listA[1]]
    b = [listA[2], listA[3]]
    c = [listA[4], listA[5]]
    d = [listA[6], listA[7]]
    if Judge(a,b,c,d) == True:
        listB.append("Yes")
    else:
        listB.append("No")
for i in range(T):
    print(listB[i])