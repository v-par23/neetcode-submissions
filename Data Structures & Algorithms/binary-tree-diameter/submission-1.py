# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # # 1. Guard against empty input
        # if not root:
        #     return 0
            
        # stack = [(root, False)]
        # max_height_dict = {}
        # diameter = 0
        
        # while stack:
        #     node, visited = stack.pop()
            
        #     if not visited:
        #         stack.append((node, True))
        #         if node.right:
        #             stack.append((node.right, False))
        #         if node.left:
        #             stack.append((node.left, False))
        #     else:
        #         left_height = max_height_dict.get(node.left, 0)
        #         right_height = max_height_dict.get(node.right, 0)
                
        #         # Update global maximum diameter found so far
        #         diameter = max(diameter, left_height + right_height)
                
        #         # Store current node's height for its parent to look up
        #         max_height_dict[node] = max(left_height, right_height) + 1
                
        # return diameter
        
        
        self.diameter = 0

        def depth(root):
            if not root:
                return 0
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter
           
