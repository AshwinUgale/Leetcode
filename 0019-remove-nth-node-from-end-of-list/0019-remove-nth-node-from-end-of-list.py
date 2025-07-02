# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodel=0
        dummy=ListNode(0,head)
        curr=head
        while curr:
            nodel+=1
            curr=curr.next

        curr=dummy
        for i in range(nodel-n):
            curr=curr.next

        curr.next=curr.next.next

        return dummy.next