class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        
        for i in range(len(nums) - 2) :          
            j, k = i + 1, len(nums) - 1
            while j < k :
                if nums[i] + nums[j] + nums[k] == 0 :
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0 :
                    k -= 1
                else :
                    j += 1
        
        return list(ans)