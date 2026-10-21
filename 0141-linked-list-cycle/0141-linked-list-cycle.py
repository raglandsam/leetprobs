# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow= head
        if slow is None or slow.next is None:
            return False
        fast=head.next.next
        while slow and fast:
            if slow is fast:
                return True
            elif not slow.next or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        