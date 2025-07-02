# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
    
        sec=slow.next
        slow.next=None
        prev=None
        while sec:
            tmp=sec.next
            sec.next=prev
            prev=sec
            sec=tmp
        
        while head and prev:
            tmp=head.next
            tmp2=prev.next

            head.next=prev
            prev.next=tmp

            head=tmp
            prev=tmp2