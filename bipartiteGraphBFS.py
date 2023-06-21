# O(n+e) time / O(n) space
def isBipartite(self, graph):
    dic = {}
    for i in range(len(graph)):
        dic[i] = graph[i]
                
    V = len(dic)
    color = [-1]*V
    for i in range(V):
        if color[i] == -1:
            if not self.bipartiteCycleCheck(i, color, dic):
                return False
    return True

def bipartiteCycleCheck(self, node, color, dic):
    queue, color[node] = [node], 1
    while(queue):
        currNode = queue.pop()
        for neighbour in dic[currNode]:
            if color[neighbour]==-1:
                color[neighbour] = 1- color[currNode]
                queue.append(neighbour)
            elif color[neighbour] == color[currNode]:
                return False
    return True 