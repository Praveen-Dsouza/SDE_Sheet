# O(n+e) time / O(n) space
def isCyclic(self, V, adj):
    visited, dfsVisited = [0]*V, [0]*V

    for i in range(V):
        if not visited[i]:
            if self.checkForCycle(i, adj, visited, dfsVisited):
                return True
    return False

def checkForCycle(self, node, adj, visited, dfsVisited):
    visited[node], dfsVisited[node] = 1, 1
    for neighbour in adj[node]:
        if not visited[neighbour]:
            if self.checkForCycle(neighbour, adj, visited, dfsVisited):
                return True
        elif dfsVisited[neighbour]:
            return True
    dfsVisited[node] = 0 # no cycle reassign dfsVisited 1 to 0
    return False

# The graph is 0 based index, for 1 based indexing 1 -> V+1