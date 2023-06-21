# O(v*e) time / O(v) space
# int(1e8) = float('inf')
def bellman_ford(V, edges, S):
    dist = [int(1e8)] * V
    dist[S] = 0

    for i in range(V):
        for u, v, wt in edges:
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    # Nth relaxation to check negative cycle
    for u, v, wt in edges:
        if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
            return [-1]

    return dist

# Without using second for loop for negative cycle detection
def bellman_ford(self, V, edges, S):
    dist = [int(1e8)] * V
    dist[S] = 0
    for i in range(V + 1):
        for u, v, wt in edges:
            if dist[u] + wt < dist[v]:
                if i == V:
                    return [-1]
                dist[v] = dist[u] + wt
    return dist