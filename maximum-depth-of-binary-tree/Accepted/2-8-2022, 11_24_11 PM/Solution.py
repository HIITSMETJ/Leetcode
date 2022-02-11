// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:            
            current_node=root
            left_depth=0
            right_depth=0
            if current_node.left:
                left_depth=self.maxDepth(current_node.left)             
            if current_node.right:
                right_depth=self.maxDepth(current_node.right) 
            return max(left_depth,right_depth)+1 
        else:
            return 0
            
            
        