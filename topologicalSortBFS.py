# O(n+e) time / O(n) space
def topoSort(V, adj):
    res, queue, indegree = [], [], [0]*V
    # count indegress
    for i in range(V):
        for x in adj[i]:
            indegree[x] += 1
            
    # get indgress with 0 and add to queue
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        # Pop the node from queue and push in res
        node = queue.pop(0)
        res.append(node)
        # traverse adjacent node of current node and decrement the indegree
        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            # if indegree 0 append to queue
            if indegree[neighbour] == 0:
                queue.append(neighbour)
            
    return res