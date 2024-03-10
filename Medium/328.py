class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        oddhead=ListNode(0)
        evenhead=ListNode(0)
        odd=oddhead
        even=evenhead
        i=1
        temp=head
        while temp:
            if(i%2!=0):
                odd.next=temp
                temp=temp.next
                odd=odd.next
                odd.next=None
            else:
                even.next=temp
                temp=temp.next
                even=even.next
                even.next=None
                
            i+=1
        oddhead=oddhead.next
        evenhead=evenhead.next
        odd.next=evenhead
        return oddhead
        
                
                
        