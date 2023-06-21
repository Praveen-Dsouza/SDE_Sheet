# O(n + e) time / O(n) space
def cloneGraph(self, node):
    oldToNew = {}
    return self.dfs(node, oldToNew) if node else None

def dfs(self, node, oldToNew):
    if node in oldToNew:
        # if already in map return the clone node
        return oldToNew[node]
    
    copy = Node(node.val)
    oldToNew[node] = copy
    for neighbor in node.neighbors:
        copy.neighbors.append(self.dfs(neighbor, oldToNew))
    return copy