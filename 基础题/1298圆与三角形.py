def Judge(a,b,r,x,y):
    #判断点是否在圆内，3个True成立则直接判不相交
    if pow((x - a),2) + pow((y - b),2) < pow(r,2):
        return 0
    elif pow((x - a),2) + pow((y - b),2) == pow(r,2):
        return 1
    else:
        return 2

def PointToLine(x1,y1,x2,y2,a,b,r):
    if x1 == x2:
        A,B,C = 1,0,-x1
    elif y1 == y2:
        A,B,C = 0,1,-y1
    else:
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
    d = (A * a + B * b + C) ** 2
    #点到直线的距离
    dist_1 = (x1 - a) * (x2 - x1) + (y1 - b) * (y2 - y1)
    dist_2 = (x2 - a) * (x1 - x2) + (y2 - b) * (y1 - y2)
    return d <= (A ** 2 + B ** 2) * (r ** 2) and dist_1 <= 0 and dist_2 <= 0

T = int(input())
listA = []
for i in range(T):
    a,b,r = map(int,input().split())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    if Judge(a,b,r,x1,y1) + Judge(a,b,r,x2,y2) + Judge(a,b,r,x3,y3) == 0:
        listA.append("No")
    elif Judge(a,b,r,x1,y1) + Judge(a,b,r,x2,y2) + Judge(a,b,r,x3,y3) < 6:
        listA.append("Yes")
    else:
        if PointToLine(x1,y1,x2,y2,a,b,r) or PointToLine(x1,y1,x3,y3,a,b,r) or PointToLine(x2,y2,x3,y3,a,b,r):
            listA.append("Yes")
        else:
            listA.append("No")
for x in listA:
    print(x)