# O(n + e) time / O(n) space
def dfsOfGraph(self, vertex, adj):
    visited, start, dfs = [0]*vertex, 0, []
    self.dfsOfGraphUtil(start, adj, visited, dfs)
    return dfs
    
def dfsOfGraphUtil(self, node, adj, visited, dfs):
    visited[node] = 1
    dfs.append(node)
    for adjacent in adj[node]:
        if not visited[adjacent]:
            self.dfsOfGraphUtil(adjacent, adj, visited, dfs)