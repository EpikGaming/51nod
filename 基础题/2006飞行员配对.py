def match(x):
    for y in listA[x]:
        if vist[y] == 0:
            vist[y] = 1
            if link[y] == -1 or match(link[y]):
                link[y] = x
                return True
    return False
m,n = map(int,input().split())
listA = [[0] * 0 for i in range(n + 1)]
link = [-1 for i in range(n + 1)]
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    listA[a].append(b)
    listA[b].append(a)
result = 0
for i in range(1,m + 1):
    vist = [0 for i in range(n + 1)]
    if match(i):
        result += 1
if result == 0:
    print("No Solution!")
else:
    print(result)