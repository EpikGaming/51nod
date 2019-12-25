import heapq
def MakeGragh(nV,nE):
    matrxi = [[0 if i  == j else float('inf') for i in range(nV)] for j in range(nV)]
    for i in range(nE):
        a,b,value = map(int,input().split())
        if a != b:
            if matrxi[a - 1][b - 1] < value:
                continue
            else:
                matrxi[a - 1][b - 1] = matrxi[b - 1][a - 1] = value
    #print(matrxi)
    route = []
    for i in range(len(matrxi)):
        route.append([])
        for j in range(len(matrxi[i])):
            if matrxi[i][j] > 0:
                route[i].append((matrxi[i][j],j))
    return route

def dijkstra_pq(conj,start):
    dis = [-1 for i in range(len(conj))]
    dis[start] = 0
    for c in conj[start]:
        dis[c[1]] = c[0]
    #print(dis)
    pool = [i for i in range(len(conj))]
    pool.remove(start)
    #print(pool)
    pq = [(dis[i],i) for i in pool if dis[i] >= 0]
    heapq.heapify(pq)
    #print(pq)
    while len(pool) > 0:
        argmin = -1
        while (argmin not in pool) and len(pq) > 0:
            MIN,argmin = heapq.heappop(pq)
        if argmin not in pool:
            break
        else:
            pool.remove(argmin)
        for c in conj[argmin]:
            if c[0] + MIN < dis[c[1]] or dis[c[1]] < 0:
                dis[c[1]] = c[0] + MIN
                heapq.heappush(pq,(dis[c[1]],c[1]))
    return dis

N,M = map(int,input().split())
conj = MakeGragh(N,M)
S,T = map(int,input().split())
listA = dijkstra_pq(conj,S - 1)
#print(listA)
print(listA[T - 1])