# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, node, maxi, mini) :
        if node :
            maxi = max(maxi, node.val)
            mini = min(mini, node.val)
            return max(self.DFS(node.left, maxi, mini), self.DFS(node.right, maxi, mini))
        else :
            return maxi - mini
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return abs(self.DFS(root, root.val, root.val))