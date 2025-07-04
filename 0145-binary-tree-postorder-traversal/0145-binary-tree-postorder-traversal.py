# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # #recursive
        # arr=[]
        # def dfs(root):
        #     if not root:
        #         return 
        #     dfs(root.left)
        #     dfs(root.right)
        #     arr.append(root.val)
        # dfs(root)
        # return arr

        #iterative
        if not root:
            return []
        stack = [root]
        visited = [False]
        arr = []
        while stack:
            cur,v=stack.pop(),visited.pop()
            if cur:
                if v:
                    arr.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return arr
