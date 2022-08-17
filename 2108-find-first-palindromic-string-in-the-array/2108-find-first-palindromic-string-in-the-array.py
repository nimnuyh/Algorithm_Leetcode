class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for x in words :
            if x == x[::-1] :
                return x
                break
        return ''