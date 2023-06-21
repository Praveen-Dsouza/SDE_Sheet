# O(e*log(v)) time / O(|e|+|v|)
import heapq

class Solution:
    # O(e*log(v)) time / O(|e|+|v|) space
    def shortestPath(self, n, m, edges):
        # Create an adjacency list of pairs of the form node1 -> (node2, edge weight)
        # where the edge weight is the weight of the edge from node1 to node2.
        adj = [[] for _ in range(n + 1)]
        for it in edges:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))

        # Create a priority queue for storing the nodes along with distances
        # in the form of a tuple (dist, node).
        pq = [(0, 1)]

        # Create a dist array for storing the updated distances and a parent array
        # for storing the nodes from where the current nodes represented by indices of
        # the parent array came from.
        dist = [float('inf')] * (n + 1)
        parent = list(range(n + 1))

        dist[1] = 0

        while pq:
            # Topmost element of the priority queue is with minimum distance value.
            dis, node = heapq.heappop(pq)

            # Iterate through the adjacent nodes of the current popped node.
            for adjNode, edW in adj[node]:
                # Check if the previously stored distance value is
                # greater than the current computed value or not,
                # if yes then update the distance value.
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))

                    # Update the parent of the adjNode to the recent
                    # node where it came from.
                    parent[adjNode] = node

        # If distance to a node could not be found, return an array containing -1.
        if dist[n] == float('inf'):
            return [-1]

        # Store the final path in the `path` array.
        path, node = [], n

        # Iterate backwards from destination to source through the parent array.
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)

        # Reverse the path array to get the final answer and then return it.
        path.reverse()
        return path
