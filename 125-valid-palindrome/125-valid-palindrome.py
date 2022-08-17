class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(x for x in s if x.isalnum())
        if s == s[::-1] :
            return True
        else :
            return False
        