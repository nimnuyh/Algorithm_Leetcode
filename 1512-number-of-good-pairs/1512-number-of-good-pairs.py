class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(len(nums)) :
            if nums.count(nums[i]) < 1 :
                continue
            else :
                for j in range(i+1, len(nums)) :
                    if nums[i] == nums[j] :
                        a += 1
        return a