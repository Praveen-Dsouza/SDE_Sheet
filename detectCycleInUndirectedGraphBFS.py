# O(n + e) time / O(n) space
def isCycle(self, V, adj):
    visited = [0]*(V+1)
    for i in range(1, V):
        if not visited[i]:
            if self.checkForCycle(i, V, adj, visited):
                return True
    return False

def checkForCycle(self, s, V, adj, visited):
    queue, visited[s] = [[s, -1]], True
    
    while queue:
        node, parent = queue.pop(0)
        for neighbour in adj[node]:
            if not visited[neighbour]: # no cycle
                visited[neighbour] = True
                queue.append([neighbour, node])
            elif parent != neighbour: # cycle already visited node
                return True
    return False