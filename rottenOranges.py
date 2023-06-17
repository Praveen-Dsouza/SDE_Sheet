# O(n * m) time / O(n * m) space
def orangesRotting(grid):
    q = []
    time, fresh = 0, 0
    
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1 #inc count for fresh
            if grid[r][c] == 2:
                q.append([r, c]) #append rotten oranges
                
    directions= [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.pop(0) #popleft coordinates and make the adjacent part rotten ie 2
            for dr, dc in directions:
                # adj 4 sides make 2(rotten)
                row, col = dr + r, dc + c
                # if not out of bounds and all oranges not rotten
                if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                    continue
                # make rotten and append coordinates
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1