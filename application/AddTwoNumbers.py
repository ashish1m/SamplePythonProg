# Definition
# for singly - linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = headRes = None
        carry = 0

        while l1 != None or l2 != None:

            if headRes == None:
                headRes = ListNode(0)
                res = headRes
            else:
                res.next = ListNode(0)
                res = res.next

            total = 0
            if l1 != None and l2 != None:
                total = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
                carry = 0

            elif l1 != None:
                total = l1.val + carry
                l1 = l1.next
                carry = 0

            elif l2 != None:
                total = l2.val + carry
                l2 = l2.next
                carry = 0

            if total > 9:
                carry = 1
                total = total % 10

            res.val = total

        if carry > 0:
            res.next = ListNode(carry)

        return headRes
