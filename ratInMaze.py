 # Solution 1: 
def directions(self, i, j, a, n, res, move, visited):
    # we are at the end of the matrix
    if i == n-1 and j == n-1:
        res.append(move)
        return
    
    # downward
    if i+1 < n and not visited[i+1][j] and a[i+1][j] == 1:
        visited[i][j] = 1
        self.directions(i+1, j, a, n, res, move + 'D', visited)
        visited[i][j] = 0
    
    # upward
    if i-1 >= 0 and not visited[i-1][j] and a[i-1][j] == 1:
        visited[i][j] = 1
        self.directions(i-1, j, a, n, res, move + 'U', visited)
        visited[i][j] = 0
    
    # right
    if j+1 < n and not visited[i][j+1] and a[i][j+1] == 1:
        visited[i][j] = 1
        self.directions(i, j+1, a, n, res, move + 'R', visited)
        visited[i][j] = 0
    
    # left
    if j-1 >= 0 and not visited[i][j-1] and a[i][j-1] == 1:
        visited[i][j] = 1
        self.directions(i, j-1, a, n, res, move + 'L', visited)
        visited[i][j] = 0
    
def findPath(self, m, n):
    res= []
    visited = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    if m[0][0] == 1:
        self.directions(0, 0, m, n, res, "", visited)
    return res

# Alternate Solution 1: 
def directions(self, i, j, a, n, res, move, vis, di, dj):
    if i == n-1 and j == n-1:
        res.append(move)
        return
    dir = 'DLRU'
    for idx in range(4):
        nexti = i + di[idx]
        nextj = j + dj[idx]
        if nexti >= 0 and nextj >=0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
            vis[i][j] = 1
            self.directions(nexti, nextj, a, n, res, move + dir[idx], vis, di, dj)
            vis[i][j] = 0
        

def findPath(self, m, n):
    res = []
    vis = [[0 for c in range(len(m))] for r in range(len(m[0]))]
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    if m[0][0] == 1:
        self.directions(0, 0, m, n, res, "", vis, di, dj)
    return res

# without using visited array
def directions(self, i, j, a, n, res, move):
    
    if i < 0 or i >= n or j < 0 or j >= n or a[i][j] == 0:
        return

    # we are at the end of the matrix
    if i == n-1 and j == n-1:
        res.append(move)
        return
    
    a[i][j] = 0
    self.directions(i + 1, j, a, n, res, move + 'D')
    self.directions(i - 1, j, a, n, res, move + 'U')
    self.directions(i, j + 1, a, n, res, move + 'R')
    self.directions(i, j - 1, a, n, res, move + 'L')
    a[i][j] = 1

def findPath(self, m, n):
    res= []
    if m[0][0] == 0 or m[n-1][n-1] == 0:
        return res
    self.directions(0, 0, m, n, res, "")
    return res