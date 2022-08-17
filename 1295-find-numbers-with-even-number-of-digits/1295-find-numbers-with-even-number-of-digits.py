class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for x in nums :
            if len(str(x)) % 2 == 0 :
                a += 1
        return a