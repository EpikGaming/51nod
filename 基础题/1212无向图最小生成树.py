def Kruskal(nodes,edges):
    result = 0
    listA = []
    for Anode,Bnode,value in edges:
        if nodes[Anode] != nodes[Bnode]:
            listA.append(((Anode,Bnode),value))
            if len(listA) == len(nodes) - 1:
                break
            a,b = nodes[Anode],nodes[Bnode]
            for i in range(len(nodes)):
                if nodes[i] == b:
                    nodes[i] = a
    for a,b in listA:
        result += b
    return result

#def Prime(nodes,edges):


N,M = map(int,input().split())
nodes = [i for i in range(N + 1)]
edges = []
for i in range(M):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x: x[2])
print(edges)
print(Kruskal(nodes,edges))