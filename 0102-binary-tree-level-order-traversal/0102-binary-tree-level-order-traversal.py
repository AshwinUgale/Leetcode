# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            lr=[]
            for i in range(len(q)):
                r = q.popleft()
                if r:
                    lr.append(r.val)
                    q.append(r.left)
                    q.append(r.right)
            if lr:
                res.append(lr)
        return res

