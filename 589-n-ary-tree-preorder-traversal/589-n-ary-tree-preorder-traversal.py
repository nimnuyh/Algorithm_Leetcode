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
            self.ans.append(node.val)

            for child in node.children :
                self.DFS(child)
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.ans = []
        self.DFS(root)
        return self.ans