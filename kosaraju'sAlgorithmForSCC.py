from collections import defaultdict

# O(n+e) time / O(n+e) space
def dfs(self, node, visited, adjList, stack):
    # Recursive function to perform Depth First Search on the graph,
    # starting from the given node. Adds visited nodes to a stack.
    visited[node] = 1
    for neighbour in adjList[node]:
        if not visited[neighbour]:
            self.dfs(neighbour, visited, adjList, stack)
    stack.append(node)

def dfs2(self, node, visited, adjListT):
    # Recursive function to perform Depth First Search on the transpose
    # of the graph, starting from the given node.
    visited[node] = 1
    for neighbour in adjListT[node]:
        if not visited[neighbour]:
            self.dfs2(neighbour, visited, adjListT)

def kosaraju(self, V, adj):
    # Implementation of Kosaraju's Algorithm to find the number of
    # Strongly Connected Components in the given graph.

    # Step 1: Perform DFS on the graph and add visited nodes to a stack.
    visited, stack = [0]*V, []
    
    for i in range(V):
        if not visited[i]:
            self.dfs(i, visited, adj, stack)

    # Step 2: Build the transpose of the graph.
    adjT = defaultdict(list)
    for i in range(V):
        visited[i] = 0
        for j in adj[i]:
            # j -> i
            # i -> j
            adjT[j].append(i)

    # Step 3: Perform DFS on the transpose of the graph, starting from
    # nodes in the order they appear on the stack. Count the number of
    # DFS trees formed to determine the number of SCCs.
    sccCount = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            sccCount += 1
            self.dfs2(node, visited, adjT)

    return sccCount
