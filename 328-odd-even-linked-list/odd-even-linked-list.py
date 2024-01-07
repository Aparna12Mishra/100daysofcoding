
class Solution(object):
    def oddEvenList(self, head):
        head1=odd=ListNode()
        head2=even=ListNode()
        t=head
        i=0
        while t:
            if i%2==0:
                even.next=t
                even=even.next
            else:
                odd.next=t
                odd=odd.next
            t=t.next
            i+=1
        odd.next=None
        even.next=head1.next
        return head2.next
            
        