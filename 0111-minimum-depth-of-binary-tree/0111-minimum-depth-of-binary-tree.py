# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # Base case: empty tree has 0 depth
        
        left_depth = self.minDepth(root.left)
        
        right_depth = self.minDepth(root.right)
        if not left_depth:
            return 1 + right_depth
        if not right_depth:
            return 1 + left_depth
        return 1 + min(left_depth, right_depth)
        