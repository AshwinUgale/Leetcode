# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        # if not root:
        #     return []
        # arr=[]
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return arr

        #iterative
        stack=[]
        arr=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            arr.append(root.val)
            root=root.right
        return arr