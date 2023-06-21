# O(n + e) time / O(n) space
def bfsOfGraph(V, adj):
    queue, visited, bfs = [0], [0]*V, []
    visited[0] = 1
    while queue:
        popVertex = queue.pop(0)
        bfs.append(popVertex)
        for neighbour in adj[popVertex]:
            if not visited[neighbour]:
                visited[neighbour] = 1
                queue.append(neighbour)
    return bfs
