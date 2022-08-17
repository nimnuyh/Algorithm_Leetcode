# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ans = []
        while head :
            ans.append(head.val)
            head = head.next
        ans_re = list(reversed(ans))
        return ans == ans_re