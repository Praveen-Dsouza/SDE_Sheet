def numIslands(grid):
    if not grid: return 0
        
    rows, cols = len(grid), len(grid[0])
    visited, islands = set(), 0
    
    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        while queue:
            row, col = queue.pop(0)
            # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] four direction
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, -1], [-1, -1], [1, 1], [0, 0]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                # if land and not visited
                if (r in range(rows) and 
                    c in range(cols) and 
                    grid[r][c] == 1 and 
                    (r, c) not in visited):
                    queue.append((r, c))
                    visited.add((r, c))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands