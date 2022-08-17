class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = list(ransomNote)
        r_b = list(ransomNote)
        m = list(magazine)
        for i in range(len(r)) :
            j = r[i]
            if j in m :
                r_b.remove(j)
                m.remove(j)
        
        return r_b == []