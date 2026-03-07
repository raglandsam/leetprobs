# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head.next==None:
            return None
        curr=head
        l=1
        while curr.next:
            curr=curr.next
            l+=1
        curr=head
        k=l//2
        for i in range(k-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
            


    
        
        