import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for n1 in range(len(nums1)) :
            heapq.heappush(heap, (nums1[n1] + nums2[0], [n1, 0]))
        
        ans = []
        while k > 0 and len(heap) > 0 :
            a = heapq.heappop(heap)
            i1 = a[1][0]
            i2 = a[1][1]
            ans.append([nums1[i1], nums2[i2]])
            if i2 < len(nums2) - 1 :
                heapq.heappush(heap, (nums1[i1] + nums2[i2 + 1], [i1, i2 + 1]))
            k -= 1
        return ans