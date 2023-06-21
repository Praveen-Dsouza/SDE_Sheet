# O(n + e) time / O(n) space
def isCycle(self, V, adj):
    visited = [0]*V
    for i in range(V):
        if not visited[i]:
            if self.checkForCycle(i, -1, visited, adj):
                return True
    return False

def checkForCycle(self, node, parent, visited, adj):
    visited[node] = 1
    for neighbour in adj[node]:
        if not visited[neighbour]:
            # has cycle
            if self.checkForCycle(neighbour, node, visited, adj): 
                return True
        elif parent != neighbour:
            return True
    return False