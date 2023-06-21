# O(e*log(v)) time / O(|e|+|v|)
import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        pq, dist = [], [float('inf')]*V
        dist[S] = 0
        heapq.heappush(pq, [0,S])
        
        while pq:
            d, node = heapq.heappop(pq)
            
            for it in adj[node]:
                ngbr, w = it[0], it[1]
                if dist[ngbr] > d + w:
                    dist[ngbr] = d + w
                    heapq.heappush(pq, [dist[ngbr], ngbr])
        return dist