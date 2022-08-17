# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        while l1 :
            num1.append(str(l1.val))
            l1 = l1.next
        while l2 :
            num2.append(str(l2.val))
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        num1 = int(''.join(num1))
        num2 = int(''.join(num2))
        num = num1 + num2
        ans = list(str(num))
        ans.reverse()
        
        ans_node = ListNode(0, None)
        answer = ans_node
        for a in ans :
            answer.next = ListNode(a, None)
            answer = answer.next
        return ans_node.next