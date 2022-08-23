# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = []
        def rec(node) :
            if node :
                if node.val <= high and node.val >= low :
                    self.ans.append(node.val)
                    rec(node.left)
                    rec(node.right)
                else :
                    rec(node.left)
                    rec(node.right)
        rec(root)
        return sum(self.ans)