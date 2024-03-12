# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list=[]
        temp=head
        while temp:
            temp_list.append(temp.val)
            temp=temp.next
        sublist_sum=0
        for i in range(len(temp_list)):
            for j in range(i + 1, len(temp_list)):
                sublist_sum = sum(temp_list[i:j+1])
                if sublist_sum == 0:
                    for k in range(i, j + 1):
                        temp_list[k] = 0
                    break
        t=ListNode(0)
        temp=t
        for i in temp_list:
            if i!=0:
                temp.next=ListNode(i)
                temp=temp.next
        return t.next              