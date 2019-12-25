import decimal

def Wythoff(a,b):
    g = (decimal.Decimal(5).sqrt() + 1) / 2
    if a > b:
        a,b = b,a
    res = (b - a) * g
    if int(res) == a:
        result = "B"
    else:
        result = "A"
    return result


n = int(input())
listA = []
for i in range(n):
    a,b = map(int,input().split())
    listA.append(Wythoff(a,b))
for x in listA:
    print(x)