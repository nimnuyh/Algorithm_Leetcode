"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def DFS(self, node) :
        if node :
            for child in node.children :
                self.DFS(child)
            self.stack.append(node.val)
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.stack = []
        self.DFS(root)
        return self.stack