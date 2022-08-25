# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def DFS(self, node):
        if not node:
            return
        self.Stack.append(str(node.val))
        # check leaf:
        if not node.left and not node.right:
            self.FinalAnswer += int(''.join(self.Stack), 2)
        self.DFS(node.left)
        self.DFS(node.right)
        self.Stack.pop()
    def sumRootToLeaf(self, root) :
        self.Stack = []
        self.FinalAnswer = 0
        self.DFS(root)
        return self.FinalAnswer