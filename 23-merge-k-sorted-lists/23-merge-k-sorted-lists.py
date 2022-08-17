# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans_heap = []
        for l in lists :
            while l :
                heapq.heappush(ans_heap, l.val)
                l = l.next
        
        ans_node = ListNode(0, None)
        pointer = ans_node
        
        while len(ans_heap) != 0 :
            pointer.next = ListNode(heapq.heappop(ans_heap), None)
            pointer = pointer.next
        
        return ans_node.next