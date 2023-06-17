# O(N^m) time / O(n) space
def graphColoring(graph, m, V):
    colourNodes = [0] * V # color array to track nodes coloured
    
    def possible(node, i):
        for j in range(V):
            if graph[node][j] == 1 and colourNodes[j] == i:
                return False
        return True
    
    def color(node, V):
        if node == V:
            return True
        for i in range(1, m + 1):
            if possible(node, i): #possible
                colourNodes[node] = i
                if color(node + 1, V) == True:
                    return True
                else:
                    colourNodes[node] = 0 # backtrack
        return False
        
    if color(0, V) == True:
        return True
    return False
