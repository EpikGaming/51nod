import math
def judge(list):
#X表示半径，L表示油量，Z表示圆心角
    for vari in list:
        X = int(vari[0])
        L = int(vari[1])
        Z = int(vari[2])
        if Z > 180:
            Z = 360 - Z
        else:
            Z = Z
        Oil = int(L) * 5
        #print(type(Oil))
        if Oil >= int(Z) * math.pi * int(X) * 2 / 180:
            print("YES")
        else:
            print("NO")
a = int(input())
varilist = []
for b in range(a):
    vari = input().split()
    varilist.append(vari)
#print(varilist)
judge(varilist)

'''
有一条圆形公路，半径为X个单位。Noder的家在这条公路上，
有一个超市也在这条公路上。家和超市所形成的圆心角为Z度。
现在车子上有L升油，一升油能开5个单位的路程。
问Noder用这L升油能不能先从家开到超市购物，然后再从超市回家。

条件题，需要注意的是当圆心角大于180度时车子是逆时针行走，
需要将圆心角转成小于180度
而且是往返，注意路程要乘2
Input：
2
1 100 0
10 0 1
Output：
YES
NO
'''