# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        curr=head
        while curr and curr.next!=None:
            ins=ListNode()
            j=gcd(curr.val,curr.next.val)
            ins.val=j
            ins.next=curr.next
            curr.next=ins
            curr=curr.next
            curr=curr.next
        return head

