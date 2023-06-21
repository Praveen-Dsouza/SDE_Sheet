# O(n+e) time / O(n) space
def topoSort(self, V, adj):
    stack, res, visited = [], [], [0]*V
    
    # Traverse for not visited nodes and call dfs
    for i in range(V):
        if visited[i] == 0:
            self.findTopoSort(i, visited, stack, adj)
            
    # After dfs pop the top element from stack and push in result array
    while stack:            
        res.append(stack[-1])
        stack.pop()
        
    return res

def findTopoSort(self, node, visited, stack, adj):
    # mark node as visited
    visited[node] = 1
    
    # Traverse the adjacent nodes of the curr node
    # if not visited call dfs and append the node in stack.
    for neighbour in adj[node]:
        if not visited[neighbour]:
            self.findTopoSort(neighbour, visited, stack, adj)
    stack.append(node)