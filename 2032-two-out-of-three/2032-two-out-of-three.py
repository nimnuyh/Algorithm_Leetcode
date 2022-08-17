class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        n12 = [num for num in nums1 if num in nums2]
        n23 = [num for num in nums2 if num in nums3]
        n31 = [num for num in nums3 if num in nums1]
        
        ans = n12 + n23 + n31
        ans = list(set(ans))
        
        return ans