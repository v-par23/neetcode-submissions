class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #intialize the queue and the time and amounut of fresh oranges as 0
        queue = deque()
        time, fresh = 0, 0

        #iterate over the entire grid
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                #count the number of fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                #idenity rotten oranges and add them to our queue to run multi-source BFS
                if grid[r][c] == 2:
                    queue.append((r, c))
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        while queue and fresh > 0:
            level_size = len(queue)
            for i in range(level_size):
                currR, currC = queue.popleft()

                for dr, dc in directions:
                    nextR, nextC = currR + dr, currC + dc
                    
                    #if orange is inbounds and fresh, make rotten
                    if nextR in range(rows) and nextC in range(cols) and grid[nextR][nextC] == 1:
                        grid[nextR][nextC] = 2
                        queue.append((nextR, nextC))
                        fresh -= 1
                    
            time += 1 
        return time if fresh == 0 else -1


