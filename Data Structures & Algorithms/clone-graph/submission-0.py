"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])
        clones = {node.val : Node(node.val)}

        while queue:
            curr = queue.popleft()
            curr_clone = clones[curr.val]

            for nei in curr.neighbors:
                if nei.val not in clones:
                    clones[nei.val] = Node(nei.val)
                    queue.append(nei)

                curr_clone.neighbors.append(clones[nei.val])
            
        return clones[node.val]
