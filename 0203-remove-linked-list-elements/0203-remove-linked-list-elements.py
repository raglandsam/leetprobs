# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        curr=head
        dum=ListNode(0,head)
        curr=dum
        while curr.next is not None:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dum.next
        