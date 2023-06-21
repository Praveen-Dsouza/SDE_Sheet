# O(e*log(e)) time / O(|e|+|v|)
import heapq
def spanningTree(V, adj):
    pq, vis, sum = [], [0]*V, 0
    heapq.heappush(pq, (0, 0))

    #  e*log(e)
    while pq:
        wt, node = heapq.heappop(pq)

        if vis[node] == 1: continue
        # add it to mst
        vis[node] = 1
        sum += wt

        # e*log(e)
        for adjNode, edW in adj[node]:
            if not vis[adjNode]:
                heapq.heappush(pq, (edW, adjNode))

    return sum