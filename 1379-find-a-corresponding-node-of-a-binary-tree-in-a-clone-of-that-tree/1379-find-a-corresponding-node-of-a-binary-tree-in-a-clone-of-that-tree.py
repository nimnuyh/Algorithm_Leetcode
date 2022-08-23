# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
        def rec(node) :
            if node :
                rec(node.left)
                if node.val == target.val :
                    self.ans = node
                rec(node.right)
        rec(cloned)
        return self.ans