class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        Srow, Scol = len(image), len(image[0])
        queue = deque([[sr, sc]])
        image[sr][sc] = color
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
            
                if 0 <= nr < Srow and 0 <= nc < Scol and image[nr][nc] == orig:
                    queue.append([nr, nc])
                    image[nr][nc] = color
        
        return image
        
        