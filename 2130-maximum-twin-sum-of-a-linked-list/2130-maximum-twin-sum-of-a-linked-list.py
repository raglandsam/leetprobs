# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxsum=-float('inf')
        curr=head
        forward=head
        forw=1
        n=0
        #finding n
        while curr:
            n+=1
            curr=curr.next
        curr=head
        c=1
        #finding node at n/2+1
        while curr and c <=n/2:
            curr=curr.next
            c+=1
        prev=None
        
        while curr:
            nxt = curr.next
            curr.next=prev
            prev= curr
            curr=nxt
        bac=n    
        while forw <= n/2 and bac>= n/2:
            maxsum=max(maxsum, forward.val+prev.val)
            forward=forward.next
            forw+=1
            prev=prev.next
            bac-=1
        return maxsum

        
        
