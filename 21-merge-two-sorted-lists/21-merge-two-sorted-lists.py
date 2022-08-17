# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0, None)
        pointer = head
        while list1 or list2 :
            if list1 and list2 :
                if list1.val < list2.val :
                    pointer.next = ListNode(list1.val, None)
                    pointer = pointer.next
                    list1 = list1.next
                else :
                    pointer.next = ListNode(list2.val, None)
                    pointer = pointer.next
                    list2 = list2.next
            elif list1 :
                pointer.next = ListNode(list1.val, None)
                pointer = pointer.next
                list1 = list1.next
            elif list2 :
                pointer.next = ListNode(list2.val, None)
                pointer = pointer.next
                list2 = list2.next
        return head.next