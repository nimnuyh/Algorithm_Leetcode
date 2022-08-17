class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        for w in s.split(' ')[:k] :
            ans = ans + w + ' '
        return ans[:-1]