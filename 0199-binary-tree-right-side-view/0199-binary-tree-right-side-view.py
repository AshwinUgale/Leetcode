# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                r=q.popleft()
                if r:
                    level.append(r.val)
                    q.append(r.left)
                    q.append(r.right)
            
            if level:
                n= level[-1]
                
                res.append(n)
        return res
