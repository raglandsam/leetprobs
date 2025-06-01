
class Solution(object):
    def reverseList(self, head) :
        curr=head
        l=[]
        while curr :
            l.append(curr.val)
            curr=curr.next
        l.reverse()
        if  not l :
            return None
        head2=ListNode(l[0])
        curr2=head2
        for i in range(1,len(l)):
            curr2.next=ListNode(l[i])
            curr2=curr2.next
        return head2