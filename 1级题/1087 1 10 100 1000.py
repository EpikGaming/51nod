def Judge(y):
    if y == 1:
        return 1
    if y == 2:
        return 1
    y = 2 * (y - 1)
    t = int(y ** 0.5)
    if (t * (t + 1)) == y:
        return 1
    return 0
T = int(input())
listA = []
for i in range(T):
    listA.append(Judge(int(input())))
for i in listA:
    print(i)