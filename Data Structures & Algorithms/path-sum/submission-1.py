# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            stack = [[root, root.val]]
        
        while stack:
            curr_node, val = stack.pop()
            
            if not curr_node.left and not curr_node.right and val == targetSum:
                return True
            
            if curr_node.left:
                stack.append((curr_node.left, curr_node.left.val + val))
            if curr_node.right:
                stack.append((curr_node.right, curr_node.right.val + val))
            
        return False
            

            

        