"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # n arry mean it is not only two nodes it also includes many childrens as well
        res=[]
        def traverse(node):
            if not node:
                return
            res.append(node.val)# first see the root since it is preorder
            #  then in these see the children from left to right 
            for child in node.children:
                traverse(child)
        traverse(root)
        return res