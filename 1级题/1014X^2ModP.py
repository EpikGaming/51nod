P,A = map(int,input().split())
listA = []
for i in range(P):
    if (i * i) % P == A:
        listA.append(i)

if listA == []:
    print("No Solution")
else:
    print(" ".join(str(i) for i in listA))