# O(n+e) time / O(n) space
def isBipartite(self, graph):
    dic = {}
    for i in range(len(graph)):
        dic[i] = graph[i]
                
    V = len(dic)
    color = [-1]*V
    for i in range(V):
        if color[i] == -1:
            if not self.bipartiteCycleCheck(dic, i, color):
                return False
    return True

def bipartiteCycleCheck(self, adj, node, color):
    if color[node] == -1: color[node] = 1

    for neighbour in adj[node]:
        # If uncolored
        if color[neighbour] == -1:
            color[neighbour] = 1- color[node]
            if not self.bipartiteCycleCheck(adj, neighbour, color):
                return False
        # If previously coloured and have same color
        elif color[neighbour] == color[node]:
            return False
    return True