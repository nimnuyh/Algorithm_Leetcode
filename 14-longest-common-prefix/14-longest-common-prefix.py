class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 :
        	return ''
        
        min_word = min(strs, key = len)
        
        for i, d in enumerate(min_word) :
            for w in strs :
                if w[i] != d :
                    return min_word[ : i]
        return min_word