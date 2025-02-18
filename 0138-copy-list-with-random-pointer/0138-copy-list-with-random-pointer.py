"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        CopyMap = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            CopyMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = CopyMap[cur]
            copy.next = CopyMap[cur.next]
            copy.random = CopyMap[cur.random]
            cur = cur.next
        
        return CopyMap[head]
