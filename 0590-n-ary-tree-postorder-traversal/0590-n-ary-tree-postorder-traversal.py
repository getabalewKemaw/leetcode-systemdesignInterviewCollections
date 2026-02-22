"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #  the same with n arry preorder but
        res=[]
        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            res.append(node.val)
        traverse(root)
        return res
