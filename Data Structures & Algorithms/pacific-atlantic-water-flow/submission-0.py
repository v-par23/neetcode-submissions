from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []
        
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] 
        
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    
                    if nr in range(rows) and nc in range(cols): 
                        if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            return visited
        
        pacificS = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlanticS = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]
        
        pacific = bfs(pacificS)
        atlantic = bfs(atlanticS)
        
        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]
