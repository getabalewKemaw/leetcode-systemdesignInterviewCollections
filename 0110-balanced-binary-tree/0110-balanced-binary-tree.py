class Solution(object):
    def isBalanced(self, root):
        def checkHeight(node):
            if not node:
                return 0
            left_h = checkHeight(node.left)
            if left_h == -1: return -1 
            
            right_h = checkHeight(node.right)
            if right_h == -1: return -1 # Already unbalanced below
            if abs(left_h - right_h) > 1:
                return -1
            return 1 + max(left_h, right_h)

        # If the result isn't -1, the tree is balanced
        return checkHeight(root) != -1
