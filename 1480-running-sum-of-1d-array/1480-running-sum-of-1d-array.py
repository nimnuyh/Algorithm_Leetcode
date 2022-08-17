class Solution(object):
    def runningSum(self, nums):
        ans = []
        c = 0
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)) :
            c += nums[i]
            ans.append(c)
        return ans