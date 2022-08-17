class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        a = []
        for i in accounts :
            a.append(sum(i))
        return max(a)