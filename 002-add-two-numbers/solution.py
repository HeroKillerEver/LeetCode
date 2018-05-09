#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = result = ListNode(0)
        carry = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            c = a + b + carry
            carry, c = c // 10, c % 10
            result.next = ListNode(c)
            result = result.next
        if carry:
            result.next = ListNode(carry)
        return root.next