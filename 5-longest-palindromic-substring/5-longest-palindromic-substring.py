class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        
        for i in range(len(s)) :
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            pal1 = s[l + 1 : r]
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            pal2 = s[l + 1 : r]
            
            ans = max(pal1, pal2, ans, key = len)
        
        return ans