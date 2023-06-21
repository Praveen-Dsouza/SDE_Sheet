# O(n+e) time / O(n) space
def isCyclic(self, V, adj):
    queue, indegree = [], [0]*V
    for i in range(V):
        for neighbour in adj[i]:
            indegree[neighbour] += 1
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
    
    cnt = 0
    while queue:
        node = queue.pop(0)
        cnt += 1
        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    # If topological sort then return False else true
    return False if cnt == V else True