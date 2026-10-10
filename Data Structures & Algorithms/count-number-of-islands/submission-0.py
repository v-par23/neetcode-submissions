class Solution:
    from collections import deque 
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def bfs(r, c):
            searchQueue = deque()
            visited.add((r, c))
            searchQueue.append((r,c))

            while searchQueue:
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                row, col = searchQueue.popleft()

                for dRow, dCol in directions:
                    neiRow, neiCol = row+dRow, col+dCol

                    if neiRow in range(rows) and neiCol in range(cols) and grid[neiRow][neiCol] == '1' and (neiRow, neiCol) not in visited:
                        visited.add((neiRow, neiCol))
                        searchQueue.append((neiRow, neiCol))

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        
        return count