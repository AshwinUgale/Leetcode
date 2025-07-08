# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,curM):
            nonlocal count
            if not root:
                return
            if root.val>=curM:
                count+=1
            curM=max(root.val,curM)
            dfs(root.left,curM)
            dfs(root.right,curM)
        dfs(root,-float('inf'))
        return count
