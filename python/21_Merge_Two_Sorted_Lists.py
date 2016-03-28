# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        res = tail = ListNode(-1)
        p1, p2 = l1, l2
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                curr = p1.val
                p1 = p1.next
            else:
                curr = p2.val
                p2 = p2.next
            tail.next = ListNode(curr)
            tail = tail.next
        while p1 is not None:
            curr = p1.val
            tail.next = ListNode(curr)
            tail = tail.next
            p1 = p1.next
        while p2 is not None:
            curr = p2.val
            tail.next = ListNode(curr)
            tail = tail.next
            p2 = p2.next
        return res.next


    # def mergeTwoLists(self, l1, l2):
    #     # recursive
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     if l1.val <= l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

